import requests
import json
import time
import random
import google.auth
from google.auth.transport.requests import Request
from src.config import PROJECT_ID, LOCATION, MODEL_NAME, FPS

# Timeout settings (in seconds)
CACHE_TIMEOUT = 120  # 2 minutes for caching
GENERATE_TIMEOUT = 300  # 5 minutes for generation (videos can take a while)

def get_credentials():
    """Gets default Google credentials."""
    credentials, project_id = google.auth.default()
    return credentials

def refresh_credentials(credentials):
    """Refreshes the Google credentials and returns headers."""
    if not credentials.valid:
        credentials.refresh(Request())
    token = credentials.token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    return headers

def prepare_requests(prompts, response_schema, video_cache, temperature):
    """Prepares the request body for Vertex AI."""
    contents_array = []
    for prompt in prompts:
        contents_array.append({
            "role": "USER",
            "parts": [{"text": prompt}]
        })

    request_array = []
    for c in contents_array:
        request_array.append({
            "cachedContent": video_cache,
            "contents": c,
            "generationConfig": {
                "responseMimeType": "application/json",
                "responseJsonSchema": response_schema,
                "temperature": temperature
            }
        })
    return request_array

def cache_video(video_uri, ttl, credentials):
    """Caches a video in Vertex AI."""
    request_body = {
        "displayName": "Test Cache",
        "model": f"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/{MODEL_NAME}",
        "contents": [{
            "role": "USER",
            "parts": [
                {
                    "fileData": {
                        "fileUri": video_uri,
                        "mimeType": "video/mp4"
                    },
                    "videoMetadata": {
                        "fps": FPS, 
                    }
                    # "mediaResolution": {"level": "MEDIA_RESOLUTION_HIGH"}
                },
            ]
        }],
        "ttl": f"{ttl}s"
    }

    url = f"https://aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/cachedContents"
    headers = refresh_credentials(credentials)

    for i in range(3):
        if i > 0:
            print("Retrying cache request...")
            time.sleep(2)
        
        try:
            response = requests.post(url, headers=headers, json=request_body, timeout=CACHE_TIMEOUT)
            if response.status_code == 200:
                return response
                
            print(f"Cache request failed: {response.status_code} {response.text}")
            if response.status_code == 401:
                headers = refresh_credentials(credentials)
                print("Authentication credentials refreshed!")
        except requests.exceptions.Timeout:
            print(f"Cache request timed out (attempt {i+1}/3)")
        except requests.exceptions.RequestException as e:
            print(f"Cache request error: {e}")
            
    raise Exception(f"Failed to cache video after retries")

def poll_vertex(prompts, response_schema, cache_name, video_uri, credentials, temperature):
    """Polls Vertex AI with the given prompts."""
    url = (
        f"https://aiplatform.googleapis.com/v1/projects/{PROJECT_ID}"
        f"/locations/{LOCATION}/publishers/google/models/{MODEL_NAME}:generateContent"
    )

    headers = refresh_credentials(credentials)
    request_array = prepare_requests(prompts, response_schema, cache_name, temperature)
    
    responses = []
    REQUEST_RETRIES = 5 
    
    for index in range(len(request_array)):
        success = False
        for i in range(REQUEST_RETRIES):
            if i > 0:
                print(f"Retrying request {index} (attempt {i+1})...")
            
            try:
                response = requests.post(url, headers=headers, json=request_array[index], timeout=GENERATE_TIMEOUT)
                
                if response.status_code == 200:
                    responses.append(response)
                    success = True
                    break
                
                print(f"Request failed: {response.status_code} {response.text}")
                
                # Cache expired
                if response.status_code == 400 or response.status_code == 404:
                    print("Cache likely expired, refreshing...")
                    cache_resp = cache_video(video_uri, 600.0, credentials)
                    cache_name = cache_resp.json()["name"]
                    # Update ALL remaining requests with new cache name
                    request_array = prepare_requests(prompts, response_schema, cache_name, temperature)
                    # Retry current request
                    continue
                
                # Auth error
                if response.status_code == 401:
                    headers = refresh_credentials(credentials)
                    print("Authentication credentials refreshed!")
                    continue
                
                # Resource exhausted
                if response.status_code == 429:
                    max_wait = min(60, 2 ** (i + 2))
                    sleep_time = random.random() * max_wait
                    print(f"Resource exhausted. Sleeping for {sleep_time:.2f}s")
                    time.sleep(sleep_time)
                    continue
                
                # Server errors - retry with backoff
                if response.status_code >= 500:
                    sleep_time = min(30, 2 ** i)
                    print(f"Server error. Sleeping for {sleep_time}s before retry...")
                    time.sleep(sleep_time)
                    continue
                    
            except requests.exceptions.Timeout:
                print(f"Request {index} timed out after {GENERATE_TIMEOUT}s (attempt {i+1}/{REQUEST_RETRIES})")
                time.sleep(5)
            except requests.exceptions.RequestException as e:
                print(f"Request exception: {e}")
                time.sleep(5)
            except Exception as e:
                print(f"Unexpected exception during request: {e}")
                time.sleep(5)
        
        if not success:
            raise Exception(f"Failed to get response for prompt {index} after {REQUEST_RETRIES} retries")

    return cache_name, responses

