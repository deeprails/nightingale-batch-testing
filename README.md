# Nightingale Batch Testing
Scripts for running the Nightingale video evaluation system in parallel

## Prerequisites
1. pip install requirements.txt
2. Save the Google Sheets service account json to your local directory
3. Copy example.py, add in video type specific information, then rename to config.py

### Saving Google Service Account
1. Navigate to [this page](https://console.cloud.google.com/iam-admin/serviceaccounts?referrer=search&project=nightingale-deeprails)
2. Click the three dots for gsheets@nightingale-deeprails.iam.gserviceaccount.com
3. Select "Manage Keys"
4. Create a new key as a JSON
5. Move the JSON file downloaded to your local machine into this repo directory at the same level as batch_runner.py
6. Rename the JSON file to 'service_account.json'

## Usage
1. Delete the /results directory if anything is present
2. List all GS URIs of the videos you'd like to evaluate in videos.txt
3. Run `python batch_runner.py --file videos.txt --output results/`, specifying --workers X if you'd like there to be X worker threads instead of the default 4
4. Confirm that result JSON files have been generated in the /results subdirectory for each of the videos in videos.txt
5. Run `python aggregator.py --dir results/`
6. Confirm results were pasted into the prompt engineering log successfully                                                       
