import tweepy
from config import getConfig

config = getConfig()

CONSUMER_KEY = config["CONSUMER_KEY"]
CONSUMER_SECRET = config["CONSUMER_SECRET"]
access_key = config["access_key"]
access_secret = config["access_secret"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

followedByMe = api.friends_ids('your @GiveUpNowMan')

for user in api.followers_ids():
    try:
        api.create_block(user)
        api.destroy_block(user)
        print('User %s is removed ' % api.get_user(user).screen_name)
    except tweepy.TweepError as errStatus:
        print(errStatus)
        if user not in followedByMe:
            api.create_block(user)
            api.destroy_block(user)
            print('User %s is removed ' % api.get_user(user).screen_name)

