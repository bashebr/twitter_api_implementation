from get_api.get_api import get_api
from api_credentials.api_credentials import get_api_credentials

def mass_unfollow(twitter_handle) -> None:
    """
    destroy all the followers of a twitter handle mass_unfollow(twitter_handle).
    """
    (consumer_key, consumer_secret, access_key, access_secret) = get_api_credentials()
    # Twitter only allows access to a users most recent 3240 tweets with this method
    API = get_api(consumer_key, consumer_secret, access_key, access_secret)
    # Get all the following users
    ids = API.get_friend_ids(screen_name=twitter_handle)
    # Unfollow all the users
    for id in ids:
        user = API.destroy_friendship(user_id=id)
        if user:
            print(f"Unfollowed {user.screen_name}")
        else:
            print(f"Failed to unfollow {user.screen_name}")
