import os
import gspread
import time
import tweepy
from functions import retweet_bot


""" If you do not have a config.py be sure to run setup first """

"""
    This commented out part grabs our premade tweets from an
    excel sheet and tweets them and then removes them from the sheet.

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("nelja-chirps").sheet1

# Update a range of cells using the top left corner address
# Example, wks.update('A1', [[1, 2], [3, 4]])
next_chirp = wks.acell('A2').value

#api.update_status(next_chirp)


# This deletes the tweet that goes out from your spreadsheet.
wks.delete_rows(2)
"""

time.sleep(2)
retweet_bot()