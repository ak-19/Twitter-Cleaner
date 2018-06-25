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

run = True
while run:
    mentionsList = api.mentions_timeline()
    if len(mentionsList) >= 1:
      for m in mentionsList:
        print("Trying to destroy " + m.text + "\n")
        try:
            m.destroy()
        except:
            print("Failed to destroy mention: ", m.id)
            run = False
            break
