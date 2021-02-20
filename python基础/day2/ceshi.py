import requests
import time

url = "http://httpbin.org/get"
# result = parse.urlparse(url)
# print(result.scheme)
# print(result.hostname)
# proxy = {"http": "http://220.174.236.211:8091"}
proxy = {"http": "http://218.59.139.238:80"}
# proxy = {"http": "http://78.47.16.54:80"}
# res = requests.Session()
time1 = time.time()
rep = requests.get(url, proxies=proxy)
time2 = time.time()
print("%.2f" % (time2 - time1))
print(rep.text)
