import os
import gspread
import time
import tweepy
from config import consumer_key, consumer_secret, access_key, access_secret

""" If you do not have a config.py be sure to run setup first """

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)


gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("nelja-chirps").sheet1

# Update a range of cells using the top left corner address
# Example, wks.update('A1', [[1, 2], [3, 4]])
next_chirp = wks.acell('A2').value

# This is the portion that sends the tweet with the given time period beneath.
api = tweepy.API(auth)
#api.update_status(next_chirp)
time.sleep(2)

# This deletes the tweet that goes out from your spreadsheet.
#wks.delete_rows(2)

allowed_games = "ElderScrolls"
tweet_numb = 1

tweets = tweepy.Cursor(api.user_timeline, allowed_games).items(tweet_numb)

def retweet_bot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Success.")
        except tweepy.TweepError as e:
            print(e.reason)

retweet_bot()