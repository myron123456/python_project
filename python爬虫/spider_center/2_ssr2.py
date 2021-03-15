# -*- codeing=utf-8 -*-
# @Time:2021/3/15 16:32
# @Author:
# @File:2_ssr2.py
# @Software:PyCharm
import requests
from fake_useragent import UserAgent
import random
import json
from lxml import etree
import time

requests.packages.urllib3.disable_warnings()
ua = UserAgent()
ua = ua.chrome
headers = {
    "user-agent": ua,
}
url = "https://ssr2.scrape.center/"
res = requests.get(url, headers=headers, verify=False, timeout=15)
# time.sleep(5)
print(res.text)
