import requests
from bs4 import BeautifulSoup
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

    with open(f'Print1_FL_{today}.txt', 'a') as fo:
        fo.write(text)

    with open(f'Print1_FL_{today}.txt','r',errors='ignore') as fo1:
        csvWriter = csv.writer(fo)
        msm = fo1.readlines()

    for i in msm:
        with open(f'Print1_FL_{today}.csv', 'a') as fo2:
            csvWriter = csv.writer(fo2)
            analysis = TextBlob(i)
            csvWriter.writerow([i, analysis.polarity, analysis.subjectivity])  



