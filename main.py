import os
import time
import tweepy
import gspread
import random
from reg_functions.functions import retweet_bot, tweet_page
from google_function.regular_tweet import regular_tweet


""" If you do not have a config.py be sure to run setup first """

# Credntial path for when calling regular_tweet.

a_list = [tweet_page, regular_tweet, retweet_bot]
credentialPath = "./google_function/credentials.json"

while True:
    #time.sleep(5)
    tweet_page()
    """
    random.choice(a_list)()
    if random.choice(a_list) == regular_tweet:
        regular_tweet(credentialPath)
    """