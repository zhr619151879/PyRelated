## Without UA camouflage:   ```User-Agent : python-requests/2.9.1```
### Obviously,Without camouflage, the server can easily identify the other party as a web crawler,**Some sites will simply reject requests when they find them coming from web crawlers**

### UA camouflage can be set up in the following way## 
```
import requests
url = 'http://httpbin.org/get'
headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64;rv:52.0) Gecko/20100101 Firefox/52.0"}
data = requests.get(url,headers = headers)
print(data.text)
```

### __Getting UA is also easy:open website->右键->检查网页->Network->选中一个请求->Header__
