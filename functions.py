import tweepy
import random
from config import consumer_key, consumer_secret, access_key, access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

allowed_games = ["ElderScrolls", "Warcraft", "DeadByBHVR", "SeaOfThieves", "FallGuysGame", "Outriders",
                "KineticGame", "ConcernedApe"]
tweet_numb = 1

tweets = tweepy.Cursor(api.user_timeline, random.choice(allowed_games)).items(tweet_numb)

def retweet_bot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Success.")
        except tweepy.TweepError as e:
            print(e.reason)