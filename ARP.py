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

sources = ['https://www.nytimes.com/','https://www.reuters.com/','https://www.wsj.com/']

for i in sources:

    page = requests.get(f'{i}')
    soup = BeautifulSoup(page.content, 'html.parser')

    if i == 'https://www.nytimes.com/':
        txt = (soup.find_all('p'))
        text = str(txt)
    elif i == 'https://www.reuters.com/':
        txt = (soup.find_all('p'))
        text = str(txt)
    else:
        txt = (soup.find_all('a'))
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
              '<p class="css-1pfq5u e1n8kpyg0">','"','<p class="css-gs67ux e1n8kpyg0">',\
              '<path d="M1 1l4.333 5L1 11" fill="none" fill-rule="evenodd" stroke="#fff" stroke-width="2">',\
              '</path>','</svg>','2q_SeZUL','%','Membership', 'style', 'column-name','?','3kGi6AN9', 'icon',\
              '16vwfuwm', 'title=', 'YouTube', 'YouTube', 'podcast', 'Z-34mcUD', 'icon', '16vwfuwm', \
              'title=', 'Podcasts', 'Podcasts', 'snapchat', 'Zoh-t3Pu', 'icon', '16vwfuwm', 'title=', \
              'Snapchat', 'Snapchat', 'googleplay', '1jhHvDOI', 'store-badge', '1fVKBhLR', '?', \
              'title=', 'Google', 'Play', 'Google', 'Play', 'appstore', 'uZsq67J9', 'store-badge', \
              '1fVKBhLR', '?', 'mt=8', 'title=', 'App', 'Store', 'App', 'Store', 'Barron', 'BigCharts',
              'Wall', 'Street', 'Journal', 'role=', 'menuitem', 'English', 'role=', 'menuitem', '', \
                      '(', 'Chinese', ')', 'role=', 'menuitem', '', '(', 'Japanese', ')', 'subscribe-link', \
                      '2kEltUj2', 'nofollow', 'Subscribe', 'Now', 'logout-link', '314o4ZBk', '?', 'Sign', 'In', \
                      'span', 'Back', 'Top', '/span', 'span', 'rotate', '2lr8F8N2', '', '/span', '?', 'Benefits',\
                      'Subscription', 'Options', '?', 'Why', 'Subscribe', '?', '?', 'Corporate', 'Subscriptions', \
                      '?', 'Professor', 'Journal', '?', 'Student', 'Journal', '?', 'High', 'School', 'Program', '?',\
                      'Amenity', 'Program', 'Customer', 'Center', 'Contact', 'Us', '?', 'Emails', '&', 'amp', \
                      'Alerts', '?', 'Guides', '?', 'My', 'News', '?', 'RSS', 'Feeds', '?', 'Video', 'Center', \
                      '?', 'Watchlist', '?', 'Podcasts', 'Advertise', 'Commercial', 'Real', 'Estate', 'Ads', 'Place', \
                      'Classified', 'Ad', 'Sell', 'Your', 'Business', 'Sell', 'Your', 'Home', 'Recruitment', '&', \
                      'amp', 'Career', 'Ads', 'Coupons', '?', 'About', 'Newsroom', 'Content', 'Partnerships', '?', \
                      'Corrections', 'Jobs', '?', 'Masthead', '?', 'News', 'Archive', 'Register', 'Free', 'Reprints', \
                      '?', 'Buy', 'Issues', 'facebook', '1HW4lqMF', 'icon', '16vwfuwm', 'title=', 'Facebook', 'Facebook',\
                      'twitter', '3QxBlupD', 'icon', '16vwfuwm', 'title=', 'Twitter','3DsLojSy', 'align-left', '3vUupbLl',\
                      'link', '37SxQ4Oy', 'h2', 'label', '264RrSh4', 'icon-position-right', '20QABGBL', \
                      'icon-relative-container', '2UDu1ihd', 'error-page', '2U383JSh', 'margin-bottom-large', \
                      '2hEWB9k8', 'styles', 'margin-bottom-large', '3azYQh7t', 'border-bottom', '1XU8HyLk', 'padding-top', \
                      '39gPkLYE', 'styles', 'padding-top', '1whmc5Ys', 'padding-bottom', '115kAeZY', 'styles', \
                      'padding-bottom', '1yk9Pn7z', 'span', 'Popular', 'Videos', '/span', 'span', 'iconLabel', \
                      '1TaG-Kv6', 'Video', 'Center', '/span', 'span', 'icon', '3fgZ6tnb', 'icon-link', '188tLWRm', \
                      'icon-relative-container', '2UDu1ihd', 'icon-position-right', '20QABGBL', '/span', '/h2', '?',\
                      'mod=error_page','section-link', '3qFFDClt', 'Opinion', 'Sadanand', 'Dhume', 'James', 'Freeman',\
                      'William', 'A.', 'Galston', 'Daniel', 'Henninger', 'Holman', 'W.', 'Jenkins', 'Andy', 'Kessler', \
                      'William', 'McGurn', 'Walter', 'Russell', 'Mead', 'Peggy', 'Noonan', 'Mary', 'Anastasia', "O'Grady",\
                      'Jason', 'Riley', 'Joseph', 'Sternberg', 'Kimberley', 'A.', 'Strassel', 'Books', 'Film', 'Television',\
                      'Theater', 'Art', 'Masterpiece', 'Series', 'Music', 'Dance', 'Opera', 'Exhibition', 'Cultural', \
                      'Commentary', 'Editorials', 'Commentary', 'Letters', 'Editor', 'Weekend', 'Interview', 'Potomac', \
                      'Watch', 'Podcast', 'Foreign', 'Edition', 'Podcast', 'Opinion', 'Notable', 'Quotable', 'opinion', \
                      'Best', 'Web', 'Newsletter', 'opinion', 'Morning', 'Editorial', 'Report', 'Newsletter', 'section-link',\
                      '3qFFDClt', 'Life', 'Arts', 'Arts', 'Books', 'Cars', 'Food', 'Drink', 'Health', 'Ideas', 'Science', 'Sports',\
                      'Style', 'Fashion', 'Travel', 'Magazine', 'Puzzles', 'Future', 'Everything', 'Far', 'Away', 'Life', 'Arts',\
                      'section-link', '3qFFDClt', 'House', 'Day', 'section-link', '3qFFDClt', 'Magazine', 'Fashion', 'Art', 'Design',\
                      'Travel', 'Food', 'Culture', 'returnLink', '235Zspdg', 'mailto', 'support', '@', 'support', '@', 'strap',\
                      'Articles', 'img', 'U.S.', 'Ban', 'Travel', 'From', 'image', '2srBg4oD', '1x', '2x', '3x','/h3', '1zGPJwbt',\
                      'div', 'image-container', '3SkfuWVV', '/', '/div', '1zGPJwbt', 'h3', 'episode-name', '3Xrkqwfv', '/h3', \
                      '1zGPJwbt', 'div', 'image-container', '3SkfuWVV', '/', '/div', '1zGPJwbt', 'h3', 'episode-name', '3Xrkqwfv',\
                      'Cookie', 'Policy', 'Copyright','3qZEiy_G', 'skipToMainButton', '-1', 'Skip', 'Main','instagram', '1nV6js1B', \
                     'Instagram', 'Instagram', 'youtube','$','brand-link', '21t2Ybqa', 'masthead-strap-link', '3Kba64tv', 'Print',\
                     'masthead-strap-link', '3Kba64tv','Privacy', 'Data', 'Subscriber', 'Agreement', 'Terms', 'Use', \
                     'cookies-advertising', 'Choices',
                     ]

    stopwords.extend(newstpwrds)

    with open(f'MSMDummy_{today}.txt', 'a') as fo:
        fo.write(text)

    with open(f'MSMDummy_{today}.txt','r',errors='ignore') as fo1:
        csvWriter = csv.writer(fo)
        msm = fo1.readlines()

    for i in msm:
        clean = []
        tokenized_var = word_tokenize(i)
        for word in tokenized_var:
            if not word in stopwords and "https" not in word \
                    and '.com' not in word \
                    and 'index' not in word \
                    and 'wsj' not in word \
                    and '=' not in word \
                    and '/' not in word \
                    and 'skip' not in word \
                    and 'Skip' not in word \
                    and 'WSJ' not in word: \

                        clean.append(str(word))

    clean1 = str(clean)

    with open(f'Print_MSM_{today}.txt', 'a')  as fo2:
        fo2.write(clean1)

    for i in clean:
        with open(f'Print_MSM_{today}.csv', 'a') as fo3:
            csvWriter = csv.writer(fo3)
            analysis = TextBlob(i)
            csvWriter.writerow([i, analysis.polarity, analysis.subjectivity]) 




