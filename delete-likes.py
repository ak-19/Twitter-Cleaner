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

for like in tweepy.Cursor(api.favorites).items():
    try:
        api.destroy_favorite(like.id)
        print("Deleted:", like.id)
    except:
        print("Failed to delete:", like.id)
