import tweepy
import os
import gspread
from config import consumer_key, consumer_secret, access_key, access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

googleSheet = 'nelja-chirps'

# Placed parameter to avoid having to hard code in credential path.
def regular_tweet(credentialPath):
    gc = gspread.service_account(credentialPath)

    # Open a sheet from a spreadsheet in one go. wks means worksheet.
    wks = gc.open(googleSheet).sheet1

    # Update a range of cells using the top left corner address
    # Example, wks.update('A1', [[1, 2], [3, 4]])
    next_chirp = wks.acell('A2').value
    api.update_status(next_chirp)

    # This deletes the tweet that goes out from your spreadsheet.
    wks.delete_rows(2)