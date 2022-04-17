# download-tweets
Download tweets of any user in CSV format

## Requirements
* Python3
* Install dependencies from `requirements.txt` via `pip install -r requirements`
* Create tweeter developer api( consumer_key, consumer_secret, access_key and access_secret) 
* Store the API keys in .env file

## Usage
* For easy use, create a virtual environment
* Then run `python main.py repo_name` and provide a repo name
* That's it

## Structure
- api_credentials: contains api credentials
- download_tweets: the main logic of downloading the tweet
- get_api: retrieves the tweet api
- main.py: mainfile
