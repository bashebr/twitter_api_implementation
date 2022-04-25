# download-tweets
Download tweets of any user in CSV format

## Requirements
* Python3
* Install dependencies from `requirements.txt` via `pip install -r requirements`
* Create tweeter developer api( consumer_key, consumer_secret, access_key and access_secret) 
* Store the API keys in .env file

## Usage
* For easy use, create a virtual environment
* Then run `python main.py module_name twitter_handle` and provide a repo name
* where `module_name` is from `mass_unfollow` and `download_tweets` and if any module is add, just use that module
* `twitter_handle`: twitter username
* That's it

## Structure
* api_credentials: contains api credentials
* download_tweets: a module for downloading tweets
* mass_unfollow: a module to unfollow mass following( not followers)
* get_api: retrieves the tweet api
* main.py: mainfile

<h2 align="center"> :two_hearts: Contribute </h2>

<p align="center">Feel free to add your own implementation via <a href="https://github.com/bashebr/twitter_api_implementation/pulls"> pull request</a> :+1:</p>
