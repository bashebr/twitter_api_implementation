from download_tweets.download_tweets import get_all_tweets

if __name__ == "__main__":
    # pass in the username of the account you want to download
    tweeter_name = input("Enter the tweeter name: ")
    get_all_tweets(tweeter_name)