import tweepy

def get_api(
    consumer_key: str,
    consumer_secret: str,
    access_token: str,
    access_token_secret: str,
) -> tweepy.API:
    """
    Returns a tweepy API object.
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)