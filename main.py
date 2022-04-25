import sys
from download_tweets.download_tweets import get_all_tweets
from mass_unfollow.mass_unfollow import mass_unfollow

if __name__ == "__main__":
    if sys.argv[1] == "mass_unfollow" and len(sys.argv) == 3:
        mass_unfollow(sys.argv[2])

    elif sys.argv[1] == "download_tweets" and len(sys.argv) == 3:
        get_all_tweets(sys.argv[1])
    else:
        print("Invalid arguments")
        print("Usage: python main.py [<mass_follow> or <download_tweets>] <screen_name>")
