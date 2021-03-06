import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import datetime
from datetime import date
import csv
from textblob import TextBlob
import time

sources = ['https://www.nba.com/','https://www.espn.com/nba/']

for i in sources:
    page = requests.get(f'{i}')
    soup = BeautifulSoup(page.content, 'html.parser')

    if i == 'https://www.nba.com/':
        txt = (soup.find_all('p'))
        text = str(txt)

    else:
        txt = (soup.find_all('h1'))
        text = str(txt)

    today = date.today()

    stopwords = nltk.corpus.stopwords.words('english')
    newstpwrds = ['.','I',';',"'s",',','--','The','the','a','an','and','<','>','p',\
            '</p>','<p>','a class="CcpaDnsLink" id="ccpa_dns_link">','NBA.com'\
            'Turner','Sports','Digital','</a>','Copyright', '',\
            '//www.nba.com/news/termsofuse','//www.nba.com/news/termsofuse',\
            'https','System','Broadcasting','CcpaDnsLink','class=','/a','NBA.com',\
            '//www.nba.com/assets/logos/turner-logo.svg','ccpa_dns_link',"''",'amp',\
            '&','A','Time','Warner','Company','Network.','//www.nba.com/news/privacy_policy.html',\
            '//www.nba.com/news/privacy_policy.html','Accessibility','/p','placeholder','|',\
            'nba_cnsnt_trst','/em','id=','Do','Not','Sell','My','Personal','Information','Turner',\
            'nbaAdChoices','href=','//www.nba.com/closed_captioning','data-entity-type=',\
            'src=',':','/','alt=','img','Inc.','data-align=','br/','more.','Terms','Use',\
            'Closed','Captioning','Entertainment','LLC'
                ]

    stopwords.extend(newstpwrds)

    with open(f'ZNBDummy_{today}.txt', 'a') as fo:
        fo.write(text)

    with open(f'ZNBDummy_{today}.txt','r',errors='ignore') as fo1:
        csvWriter = csv.writer(fo1)
        msm = fo1.readlines()

    for i in msm:
        clean = []
        tokenized_var = word_tokenize(i)
        for word in tokenized_var:
            if not word in stopwords and "h1" not in word \
                    and "contentItem" not in word \
                    and "=" not in word and "__" not in word\
                    and "-" not in word:
                        clean.append(str(word))

    clean1 = str(clean)
    period = "."
    add = [i for i in clean1 if i.isalpha() or i.isspace() or i in period]
    add1 = "".join(add)

    with open(f'Print_NBA_{today}.txt', 'a') as fo2:
        fo2.write(add1)

    for i in clean:
        with open(f'Print_NBA_{today}.csv', 'a') as fo3:
            csvWriter = csv.writer(fo3)
            analysis = TextBlob(i)
            csvWriter.writerow([i, analysis.polarity, analysis.subjectivity])  











