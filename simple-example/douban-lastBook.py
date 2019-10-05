'''
    Grab the new book douban launched information
'''

"""
 second comment 
"""

import requests
from bs4 import BeautifulSoup

url = 'https://book.douban.com/latest'  #url
headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64;rv:52.0) Gecko/20100101 Firefox/52.0"}  # Camouflage header
data = requests.get(url, headers=headers)

# parse data
soup = BeautifulSoup(data.text, 'lxml')

# left column
book_left = soup.find('ul', {'class': 'cover-col-4 clearfix'})
book_left = book_left.find_all('li')

# right column
book_right = soup.find('ul', {'class': "cover-col-4 pl20 clearfix"})
book_right = book_right.find_all('li')
#class="cover-col-4 pl20 clearfix"

# merge two lists
books = list(book_right) + list(book_left)

# Do the same for each book block, acquire information
img_urls = []
titles = []
ratings =[]
authors = []
details = []

for book in books:
    # the URL of book cover
    img_url = book.find('a').find('img').get('src')  # find the first Label a
    img_urls.append(img_url)

    # the book title
    title = book.find_all('a')[1].get_text()
    titles.append(title)

    # Evaluation of star
    rating = book.find('p', {'class': 'rating'}).get_text()
    rating = rating.replace('\n', '').replace(' ', '')  # replace \n and space
    ratings.append(ratings)

    # author and published information
    author = book.find('p',{'class': 'color-gray'}).get_text()
    author = author.replace('\n', '').replace(' ', '')
    authors.append(author)

    # book description
    detail = book.find_all('p')[2].get_text()
    detail = detail.replace('\n', '').replace(' ', '')
    details.append(detail)

# print content

print('img_urls: ', img_urls)
print('titles: ', titles)
print('ratings: ', ratings)
print('authors: ', authors)
print('details: ', details)

