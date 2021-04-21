import os
import time
import tweepy
from config import consumer_key, consumer_secret, access_key, access_secret

""" If you do not have a config.py be sure to run setup first """

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
os.chdir('images')
for game_image in os.listdir('.'):
    api.update_with_media(game_image)
    time.sleep(5)