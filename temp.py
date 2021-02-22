import requests
from fake_useragent import UserAgent

requests.packages.urllib3.disable_warnings()

ua = UserAgent()
ua = ua.random
headers = {
    "User-Agent": ua,

}
# url = "https://so.csdn.net/api/v2/search?q=python+%E7%88%AC%E8%99%AB&t=userinfo&p=1&s=0&tm=0&lv=-1&ft=0&l=&u=&platform=pc"
url = "http://113.31.118.145:8206"
res = requests.get(url=url, headers=headers, verify=False,
                   timeout=15, allow_redirects=False)
print(res.text)
