import requests
import time
import os
import chardet
from bs4 import BeautifulSoup
from MEmail import send_ms


# get web data
def get_web_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT6.1; WOW64) AppleWeb"
                      "Kit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36 "}
    html = requests.get(url, headers=headers)
    Encoding = chardet.detect(html.content)['encoding']  # Coding detection and setting
    html.encoding = Encoding
    web_data = html.text
    return web_data


# we found that the title is usually under the tag a
# and they generally contain target attribute, corresponding to the value of _blank

# get titles and corresponding links
def get_titles(web__data):
    title_hrefs = {}
    soup = BeautifulSoup(web__data, 'lxml')
    title_data = soup.find_all({'a': {'target': '_blank'}})

    for title in title_data:
        title__text = title.get_text()

        # filter out irrelevant tags(generally is short)
        if len(title__text) >= 10:
            if title.has_attr('href'):  # if title has a link
                href = title['href']

            else:
                href = 'Cannot find a link...'

            title_hrefs[title__text] = href
    return title_hrefs


# Filter the information you want (whether include keyword）
def get_roi(title_hrefs, key_words):
    roi = {}  # used to store titles of interest
    for title in title_hrefs:
        if key_words in title:
            roi[title] = title_hrefs[title]

    return roi


def send_report(roi):
    length = len(roi)
    s1 = str(length) + ' related news were detected' + '\n'
    s2 = ''
    for title in roi:
        s2 += title
        s2 += roi[title]
        s2 += '\n'
    send_ms(s1 + s2)


# generate local logging
def record(roi, key_words):
    if 'NewsReportLog.txt' not in os.listdir():
        with open('NewsReportLog.txt', 'w') as f:  # write mode
            f.write(str(key_words) + 'Related news capture program log ' + str(time.ctime()) + '\n')

    with open('NewsReportLog.txt', 'a') as f:  # append mode
        f.write('=' * 10 + str(time.ctime() + '=' * 10))
        for title in roi:
            f.write(title)
            f.write(roi[title])
        f.write('\n')


if __name__ == '__main__':
    web_data = get_web_data('http://tech.baidu.com/')
    titles = get_titles(web_data)
    key_words = 'iphone'
    roi = get_roi(titles, key_words)
    print(roi)
    if len(roi) != 0:
        record(roi, key_words)
        send_report(roi)
