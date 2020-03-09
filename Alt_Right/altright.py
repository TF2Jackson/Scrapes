#!/usr/bin/python3
# coding: utf-8

# In[4]:


# Professor King:
# Thanks for agreeing to take a look at this.  Up front: I do not
# have, nor have I attempted to write, code in this file which
# would automate.  None of my StackOverflow research turned up suggestions
# for doing this; instead everyone there emphasized trying to use the
# crontab function in Terminal, or using a service like Amazon Web Service.

# Concede I might not have looked in the write place--but I will say that
# I spent the better part of two weeks trying to chase down solutions for
# those two courses of action.

# The rest of this notebook explains the code I am using in a manual way.
# It probably can be made more efficient--but it does get the job done,
# albeit requiring manual scraping.



# Input my keys and tokens from Twitter; allows use of Tweepy API

CONSUMER_KEY = 'a19MLVL0NMt7ByLp74Ey0hFN7'
CONSUMER_KEY_SECRET = 'q2KiIFKpwoLqXIIOjNAZ4zEm8h9Vmvwp8X3drcr0WeiLepdJYt'
ACCESS_TOKEN = '1167467648181035008-8PqoqisYZTNwAHxvmd6QqYmH2ztS6a'
ACCESS_TOKEN_SECRET = 'FnXJhL4a50kSTb5Bzr1Ix6cIfnXG6XxvrAPtPU7gmiyal'

# Import dependencies and libraries 

import csv
    # We write the scraped tweets into a .csv file to a) run it through LIWC easily and b) generate graphics
    # to give us quick looks at variability of things like frequency, sentiment, etc over time.  Provides
    # us an at-a-glance look at trends
import datetime
    # Allows me to set search parameters so that I only get each day's tweets and don't have to sort through
    # the old tweets in resultant .csv files
from datetime import date
    # This allows us to name each .csv file with a unique identifier.  That way, when I run the code, instead of
    # overwriting yesterday's tweets, I get a file with today's DTG.
import tweepy
    # We scrape using the Tweepy API
from textblob import TextBlob
    # textblob can be run automatically on each tweet as it is scraped; it is a secondary check on LIWC.  As you've
    # suggested, there probably are better options--but this is the one that I found that worked and was easy for
    # both to comprehend and implement with my skills at the time.

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
    # These are all required in order to make the Tweepy API function 
    
    # Drop code into server that runs it every once in a while.

today = date.today()

    # This is how I ensure that I am only scraping today's tweets.  I have to manually change the dates
    # every day when I run the program.

csvFile = open(f'#Alt_Right_{today}.csv2', 'a')
csvWriter = csv.writer(csvFile)
    # This is how I write the scraped tweets into a .csv file and give it a unique name for each day

hashtags = ['#14Words','#Boogaloo','#ISaluteWhitePeople','#WhiteGenocide','#TCOT','#QAnon']
    # Each control group has its own list, populated with the actionable / practicable hashtags
    # and keywords we uncovered in the process of writing our ideological lit review
    
    # Note: last semester I didn't know how to do this...and so I literally had a Python file for
    # every single individual hashtag.  So instead of running one program for an entire group...
    # I was running about 25 different programs, separated by 15 minutes each.  This is what 
    # I was referencing when I said that the Intro to Python class has really improved efficiency.
  
for i in hashtags:
    # We iterate a for loop to cycle through all of the keywords and hashtags in our hashtag list
    for tweet in tweepy.Cursor(api.search, q=i, count=100000,                                                    lang="en",                                                    ).items():

        tweet_dtg = str(tweet.created_at)
        todays = str(today)

        if todays in tweet_dtg:
            print(tweet.created_at, tweet.text, tweet.user.location)

            analysis = TextBlob(tweet.text)
            print(analysis.sentiment_assessments)

            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.location, analysis.polarity, analysis.subjectivity])



Alt_Right alt.py
