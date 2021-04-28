import os
import time
import tweepy
import gspread
from reg_functions.functions import retweet_bot, tweet_page
from google_function.regular_tweet import regular_tweet


""" If you do not have a config.py be sure to run setup first """

credentialPath = "./google_function/credentials.json"
time.sleep(2)
tweet_page()