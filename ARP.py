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

sources = ['https://www.radixjournal.com/','https://www.amren.com/']

for i in sources:
    page = requests.get(f'{i}')
    soup = BeautifulSoup(page.content, 'html.parser')

    if i == 'https://www.radixjournal.com/':
        txt = (soup.find_all('p'))
        text = str(txt)
    else:
        txt = (soup.find_all('a'))
        text = str(txt)

    today = date.today()

    stopwords = nltk.corpus.stopwords.words('english')
    newstpwrds = ['.','I',';',"'s",',','--','The','the','a','an','and','<','>','p',\
            '[', '','/p','', 'href=', "''", '#', '_3znysh7', "''", '[', '1',\
            ']', '/a', '/p','/p', 'href=', "''", '#', '_30j0zll', "''", '[', \
            '1', ']', '/a','href=', "''", '#', '_2et92p0', "''", '[', '2', ']',\
            '/a','publications', '/i', 'href=','https','/em','(', 'AC', '', '59',\
            '(', 'EH', ':', '3', ')','em','sup', 'class=', 'footnote', 'fn16', \
            'id=', 'ffn16', '16', '/sup','(', 'Z', ':', '11', ')','script', \
            'async=', 'charset=', 'utf-8', 'true', 'src=', '/script', 'Type', \
            'field', 'hit', 'Enter/Return', 'search'
            ]

    stopwords.extend(newstpwrds)

    with open(f'ZARDummy_{today}.txt', 'a') as fo:
        fo.write(text)

    with open(f'ZARDummy_{today}.txt','r',errors='ignore') as fo1:
        csvWriter = csv.writer(fo1)
        msm = fo1.readlines()

    for i in msm:
        clean = []
        tokenized_var = word_tokenize(i)
        for word in tokenized_var:
            if not word in stopwords and "mediamatters" not in word \
                    and "vanityfair" not in word \
                    and "" not in word \
                    and "journal" not in word \
                    and ".com" not in word \
                    and "t.co" not in word \
                    and "html" not in word \
                    and 'gwh=' not in word \
                    and "www" not in word: \
                        clean.append(str(word))

    clean1 = str(clean)

    with open(f'Print_AR_{today}.txt', 'a')  as fo2:
        fo2.write(clean1)

    for i in clean:
        with open(f'Print_AR_{today}.csv', 'a') as fo3:
            csvWriter = csv.writer(fo3)
            analysis = TextBlob(i)
            csvWriter.writerow([i, analysis.polarity, analysis.subjectivity]) 






