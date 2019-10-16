import re
import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}
# print(headers)
html = requests.get('https://www.baidu.com/', headers=headers)
html.encoding = 'utf-8'
html = html.text
# print(html)

# r mean avoid escape word like '/n'
title = re.findall(r'<a href="(http://.*?.com)" name="tj_tr.*?" class="mnav">(\w{2})</a>', html)
print(title)

