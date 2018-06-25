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

for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
        print("Deleted:", status.id)
    except:
        print("Failed to delete:", status.id)
