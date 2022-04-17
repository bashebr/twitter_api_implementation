from decouple import config

# Twitter API credentials
consumer_key = config("CONSUMER_KEY")
consumer_secret = config("CONSUMER_SECRET")
access_key = config("ACCESS_KEY")
access_secret = config("ACCESS_SECRET")

def get_api_credentials() -> tuple:

    """
    Returns a tuple of credentials.
    """
    return (
        consumer_key,
        consumer_secret,
        access_key,
        access_secret,
    )