CONSUMER_KEY = 'a19MLVL0NMt7ByLp74Ey0hFN7'
CONSUMER_KEY_SECRET = 'q2KiIFKpwoLqXIIOjNAZ4zEm8h9Vmvwp8X3drcr0WeiLepdJYt'
ACCESS_TOKEN = '1167467648181035008-8PqoqisYZTNwAHxvmd6QqYmH2ztS6a'
ACCESS_TOKEN_SECRET = 'FnXJhL4a50kSTb5Bzr1Ix6cIfnXG6XxvrAPtPU7gmiyal'

import datetime
from datetime import date
import csv
import tweepy
from textblob import TextBlob
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

today = date.today()

hashtags = ['#Politics','#Election','#Economy']

while True:
    with open(f'#Control_nrt_{today}.csv', 'a') as fo:
        csvWriter = csv.writer(fo)
        t = 0

        for i in hashtags:
            for tweet in tweepy.Cursor(api.search, q=i, count=100000, \
                                        lang = "en", \
                                        ).items():

                tweet_dtg = str(tweet.created_at)
                todays = str(today)

                if todays in tweet_dtg:
                    
                    if (not tweet.retweeted) and ('RT ' not in tweet.text):
                        analysis = TextBlob(tweet.text)
                        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.location, analysis.polarity, analysis.subjectivity])

                        text = str(tweet.text)

                        with open(f'#Control_nrt_{today}.txt', 'a') as fo1:
                            fo1.write(text)
                                
                        t = t+1

                        if t >= 4000:
                            time.sleep(900.0)
                            t = 0




