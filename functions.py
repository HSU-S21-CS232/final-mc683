import tweepy
import random
import os
import gspread
from config import consumer_key, consumer_secret, access_key, access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

allowed_games = ["ElderScrolls", "Warcraft", "DeadByBHVR", "SeaOfThieves", "FallGuysGame", "Outriders",
                "KineticGame", "ConcernedApe"]




def retweet_bot():
    tweet_numb = 1
    tweets = tweepy.Cursor(api.user_timeline, random.choice(allowed_games)).items(tweet_numb)
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Success.")
        except tweepy.TweepError as e:
            print(e.reason)

def normal_tweet():
    gc = gspread.service_account('credentials.json')

    # Open a sheet from a spreadsheet in one go. wks means worksheet.
    wks = gc.open("nelja-chirps").sheet1

    # Update a range of cells using the top left corner address
    # Example, wks.update('A1', [[1, 2], [3, 4]])
    next_chirp = wks.acell('A2').value
    api.update_status(next_chirp)

    # This deletes the tweet that goes out from your spreadsheet.
    wks.delete_rows(2)

def tweet_page():
    tweets = api.mentions_timeline()
    for tweet in tweets:
        if '#warcraft' in tweet.text.lower():
            print('twitter.com/Warcraft')