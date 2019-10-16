'''
Simulate login by form
'''
import time
import requests
import pickle
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


# Submit the form and get the cookie
def login_and_getdata():
    pass


def get_cookie_from_net():
    url = 'https://accounts.douban.com/login'
    # creat a form
    payload = {'sourece': 'Node',
               'redir': 'https://www.douban.com/',
               'form_email': '填写登录邮箱',
               'form_password': '填写登录密码',
               'login': '登录'}

    data = s.post(url, headers=headers, data=payload, verify=True)  # skip the SSL verification

    with open('cookies.douban', 'wb') as f:
        cookiedict = requests.utils.dict_from_cookiejar(s.cookies)
        pickle.dump(cookiedict, f)
    print("submitted form login,  cookies successfully...")
    time.sleep(1)
    return s.cookies


# get cookie from file cookie
def get_cookie_from_file():
    with open('cookies.douban', 'rb') as f:
        cookiedict = pickle.load(f)
        cookies = requests.utils.cookiejar_from_dict(cookiedict)
    print('parsed file, extract cookies successfully...')
    time.sleep(1)
    return cookies


# surpose get ur signature data here
def getdata(html):
    soup = BeautifulSoup(html.text, 'lxml')
    mydata = soup.select('#display')[0].get_text()
    '''
    Acquire and store other data after login ，here just the signature data
    '''
    return mydata


def login_and_getdata():
    print('get cookies...')
    try:
        s.cookies = get_cookie_from_file()

    except:

        print('Failed to get data from file...\n now trying to submit the form login to get it...')
        time.sleep(1)
        s.cookies = get_cookie_from_net()
    html = s.get('https://www.douban.com/people/146448257/', headers=headers)
    data = getdata(html)
    print(data)


if __name__ == '__main__':
    # some global variable
    s = requests.session()
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    login_and_getdata()

