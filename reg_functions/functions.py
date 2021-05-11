import tweepy
import random
import os
import gspread
from reg_functions.game_twitter import allowed_games, games_page
from config import consumer_key, consumer_secret, access_key, access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)



FILE_NAME = './reg_functions/last_seen.txt'
tweet_numb = 1

def retweet_bot():
    tweets = tweepy.Cursor(api.user_timeline, random.choice(games_page)).items(tweet_numb)
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Success.")
            # Create favorite is the "like" option
            api.create_favorite(tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def tweet_page():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        for games in allowed_games:
            if games.lower() in tweet.full_text.lower():
                game = games[1:]
                api.update_status('@' + tweet.user.screen_name + f' This games page is twitter.com/{game}.', tweet.id)
                store_last_seen(FILE_NAME, tweet.id)
                print("page printed")
                break