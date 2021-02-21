#coding=u
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
import json
requests.packages.urllib3.disable_warnings()

global result_list
result_list = []
def crawel_ribang(url):
    user_agent = UserAgent()
    ua = user_agent.random
    headers = {
        "User-Agent": ua,
    }
    # proxy = {'http': 'http://112.246.233.201:8060'}
    proxy ={"http": "http://5.39.17.96:80"}
    res = requests.get(url=url, headers=headers, verify=False,proxies=proxy,timeout=15)
    print(res.text)
    return res.text

def main():
    url = "http://www.ithome.com/###"
    crawel_ribang(url)
main()