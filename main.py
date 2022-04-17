import sys
from download_tweets.download_tweets import get_all_tweets

if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_all_tweets(sys.argv[1])
    else:
        print("Usage: python main.py <screen_name>")