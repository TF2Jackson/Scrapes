#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup
import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import datetime
from datetime import date
import csv
from textblob import TextBlob
import time

sources = ['https://deepgreenresistance.org/en/','https://earthfirstjournal.org/','https://dgrnewsservice.org/']

for i in sources:
    page = requests.get(f'{i}')
    soup = BeautifulSoup(page.content, 'html.parser')
    
    if i == 'https://deepgreenresistance.org/en/':
        txt = (soup.find_all('p'))
        text = str(txt)
    elif i == 'https://earthfirstjournal.org/':
        txt = (soup.find_all('a'))
        text = str(txt)
    else:
        txt = (soup.find_all('h1'))
        text = str(txt)
                        
    today = date.today()

    stopwords = nltk.corpus.stopwords.words('english')
    newstpwrds = ['.','I',';',"'s",',','--','The','the','a','an','and','<','>','p',\
            '/a','class=','accordion-toggle',"''",'data-parent=','#','main_nav',\
            'data-toggle=','//earthfirstjournal.org/store/product/earth-first-journal-subscription/',\
            'media-heading','//earthfirstjournal.org/newswire/2019/10/07/were-back/','href=','http',\
            '/h5', '/p', '/a','media-heading', "''", 'Subscribe', '/h5','//armedwithvisions.com/',\
            'main_nav', "''", 'data-toggle=', "''", 'collapse',"''", 'https', ':', \
            '//greenflame.libsyn.com/rss', "''", 'img', 'alt=', "''", 'RSS', "''", 'class=', "''",\
            'Pages', '/h1', 'h1', 'class=', "''", 'widget-title', "''", 'Archives', '/h1', 'h1', \
            'class=', "''", 'widget-title','h5','//earthfirstjournal.org/favorite-blogs',\
            '//earthfirstjournal.org/indigenous-rights-and-environmental-justice',\
            'Favorite', 'Blogs','left=', 'no-repeat=', 'src=', \
            '//earthfirstjournal.org/wp-content/themes/monkey-wrenched/images/newswire-tag.png',\
            'top=', '/', 'pull-left','mailto', 'collective', '@', 'earthfirstjournal.org', \
            'collective', 'earthfirstjournal.org', 'aria-current=', 'page', '//earthfirstjournal.org/',\
            'Earth', 'First', '!', '//earthfirstjournal.org/about/', 'About', 'Earth', 'First', '!', \
            '//earthfirstjournal.org/submissions/', 'Submissions', '//earthfirstjournal.org/contact/', \
            'Contact', '//earthfirstjournal.org/donate/', 'Donate', 'mailto', 'collective', '@', \
            'earthfirstjournal.org', 'collective', 'earthfirstjournal.org',\
            '//app.e2ma.net/app2/audience/signup/1730470/1719566/', '?', 'v=a', 'Sign', ']', '[', \
            'site-title', '//dgrnewsservice.org/', 'rel=', 'home', 'Deep', 'Green', 'Resistance', \
            'News', 'Service', 'entry-title','rel=', 'bookmark','suwet', '', 'en', 'First', 'Nation',\
            'screen-reader-text', 'Posts', 'navigation', 'Search', '&', 'amp', 'Filter', 'DGR', 'updates',\
            'Recent', 'Comments', 'Top', 'Posts', '&', 'amp', 'Feed', 'rsswidget', 'rss-widget-icon', \
            'height=', '14', 'src=', '//dgrnewsservice.org/wp-includes/images/rss.png', 'style=', \
            'border:0', 'width=', '14', '/', 'rsswidget', '//greenflame.libsyn.com/', 'Green', \
            'Flame', 'podcast', 'What', 'Is', 'Deep', 'Green', 'Resistance', '?', 'Links',"title=",\
            'target=', '_blank','media-object', 'wp-post-image'
            ]
                        
    stopwords.extend(newstpwrds)

    with open(f'Print_FL_{today}.txt', 'a') as fo:
        fo.write(text)

    with open(f'Print_FL_{today}.txt','r',errors='ignore') as fo1:
        csvWriter = csv.writer(fo)
        msm = fo1.readlines()

    for i in msm:
        clean = []
        tokenized_var = word_tokenize(i)
        for word in tokenized_var:
            if not word in stopwords and "earthfirstjournal" not in word \
                    and "dgrnewsservice" not in word \
                    and "deepgreenresistance" not in word and "tab" not in word:
                clean.append(str(word))

    for i in clean:
        with open(f'Print_FL_{today}.csv', 'a') as fo2:
            csvWriter = csv.writer(fo2)
            analysis = TextBlob(i)
            csvWriter.writerow([i, analysis.polarity, analysis.subjectivity])  
            


