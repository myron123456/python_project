import requests
import time
from fake_useragent import UserAgent
requests.packages.urllib3.disable_warnings()
ua = UserAgent()
ua = ua.random
print(ua)
headers = {
        "User-Agent": ua,

    }
url = "http://httpbin.org/get"
# result = parse.urlparse(url)
# print(result.scheme)
# print(result.hostname)
# proxy = {"http": "http://220.174.236.211:8091"}
# proxy = {"http": "http://218.59.139.238:80"}
# proxy = {"http": "http://78.47.16.54:80"}
# proxy ={"http": "http://5.39.17.96:80"}
# proxy ={'http': 'http://191.101.39.27:80'}
# proxy = {'http': 'http://49.204.79.81:80'}
# proxy = {'http': 'http://14.97.26.195:80'}
proxy = {'http': 'http://8.210.153.2:80'} #特殊
# proxy ={'http': 'http://112.246.233.201:8060'}
# proxy = {'http': 'http://195.169.35.228:8080'} #特殊
# proxy = {'http': 'http://89.187.177.107:80'} #太多连接
# proxy = {"http": "http://161.202.110.154:12345"}
# proxy = {"http": "http://106.14.198.6:8080"}
# proxy  = {'http': 'http://136.233.215.137:80'}

# res = requests.Session()
time1 = time.time()
rep = requests.get(url, headers=headers,proxies=proxy,timeout=15)
time2 = time.time()
print("%.2f" % (time2 - time1))
print(rep.text)
