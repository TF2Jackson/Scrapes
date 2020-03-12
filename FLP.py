import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
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
            'viewbox=','e1n8kpyg0','css-1pfq5u','class=','news','[',']','/p',\
            '"','fff',"''",'d=','evenodd','fill-rule=','viewbox=','#','stroke=',\
            '1l4.333', '5L1', '11', 'fill=','height=','get.', 'css-1qo9wc0', 'We', \
            '', 'like', 'thoughts', 'New', 'York', 'Times', 'home', 'page', \
            'experience.', 'href=', 'http', ':', '//nyt.qualtrics.com/jfe/form/SV_eFJmKj9v0krSE0l', \
            'rel=','noopener', 'noreferrer', 'target=', '_blank', 'Let', 'us', 'know',\
            'think', '/a', 'svg', '0', '0', '7', '12', 'width=', '7', 'path', 'M1', \
            'none', 'stroke-width=', '2', '/path', '/svg','css-gs67ux','/info/disclaimer',\
            'Reuters','Reuters.com','id=','``','newstipInfo','//thomsonreuters.com/','</p>', '</a>',\
            '<p class="css-1pfq5u e1n8kpyg0">','"','<p class="css-gs67ux e1n8kpyg0">', \
            '<path d="M1 1l4.333 5L1 11" fill="none" fill-rule="evenodd" stroke="#fff" stroke-width="2">', \
            '</path>','</svg>']

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
            if not word in stopwords:
                clean.append(str(word))

    for i in clean:
        with open(f'Print_FL_{today}.csv', 'a') as fo2:
            csvWriter = csv.writer(fo2)
            analysis = TextBlob(i)
            csvWriter.writerow([i, analysis.polarity, analysis.subjectivity])  



