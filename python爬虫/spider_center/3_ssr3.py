# -*- codeing=utf-8 -*-
# @Time:2021/3/15 16:35
# @Author:
# @File:3_ssr3.py
# @Software:PyCharm
import requests
from fake_useragent import UserAgent
from requests.auth import HTTPBasicAuth
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
user = "admin"
password = "admin"
res = requests.get(url, headers=headers, auth=HTTPBasicAuth(user, password), verify=False, timeout=15)
# time.sleep(5)
# print(res.text)

# def way_2():
#     headers['Authorization'] = "Basic YWRtaW46YWRtaW4="
#     headers['Referer'] = "https://scrape.center/"
#     res1 = requests.get(url, headers=headers, verify=False,timeout=15)
#     print(res1.text)
