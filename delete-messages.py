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

for m in api.direct_messages():
    print("Trying to destroy " + m.text + "\n")
    try:
        m.destroy()
    except:
        print("Failed to destroy " + m.text + "\n")

for m in api.sent_direct_messages():
    print("Trying to destroy " + m.text + "\n")
    try:
        m.destroy()
    except:
        print("Failed to destroy " + m.text + "\n")
