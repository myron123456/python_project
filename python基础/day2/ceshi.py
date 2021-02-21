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
proxy ={"http": "http://5.39.17.96:80"}
# proxy ={'http': 'http://191.101.39.27:80'}
# proxy = {'http': 'http://49.204.79.81:80'}
# proxy = {'http': 'http://14.97.26.195:80'}
proxy = {"http": "http://88.99.10.254:1080"}
# res = requests.Session()
time1 = time.time()
rep = requests.get(url, headers=headers,proxies=proxy,timeout=15)
time2 = time.time()
print("%.2f" % (time2 - time1))
print(rep.text)
