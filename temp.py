import requests
from fake_useragent import UserAgent

requests.packages.urllib3.disable_warnings()

ua = UserAgent()
ua = ua.random
headers = {
    "User-Agent": ua,

}
# url = "https://so.csdn.net/api/v2/search?q=python+%E7%88%AC%E8%99%AB&t=userinfo&p=1&s=0&tm=0&lv=-1&ft=0&l=&u=&platform=pc"
# url = "http://113.31.118.145:8206"
url = "http://httpbin.org/get"
# proxy ={'http': 'http://89.187.177.107:80'}
# proxy = {'http': 'http://8.210.153.2:80'}
# proxy = {'http': 'http://218.60.8.99:3129'} #特殊，返回两个
# proxy = {'http': 'http://60.205.132.71:80'} #特殊
# proxy = {'http': 'http://15.237.10.173:8080'} #特殊
proxy = {'http': 'http://39.98.39.55:80'}
res = requests.get(url=url, headers=headers, verify=False,
                   timeout=15, allow_redirects=False,proxies=proxy)
print(res.text,res.status_code)
