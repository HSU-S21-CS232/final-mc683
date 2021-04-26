import os
import gspread
import time
import tweepy
from functions import retweet_bot, normal_tweet


""" If you do not have a config.py be sure to run setup first """

time.sleep(2)
normal_tweet()