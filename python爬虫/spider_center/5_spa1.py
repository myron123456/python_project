# -*- codeing=utf-8 -*-
# @Time:2021/3/15 17:06
# @Author:
# @File:5_spa1.py
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


def crawel(url):
    headers = {
        "user-agent": ua,
    }
    res = requests.get(url, headers=headers, verify=False, timeout=15)
    # time.sleep(5)
    # print(res.text)
    return res.text


def parse_xpath(html):
    results = []
    html = json.loads(html)
    for i in range(0, 10):
        result_dict = {}  # 注意字典的位置
        result_dict['title'] = html['results'][i]['name']
        result_dict['score'] = html['results'][i]['score']
        result_dict['type'] = ";".join(html['results'][i]['categories'])
        print(result_dict)
        # print(result_dict['type'])
        results.append(result_dict)
    # print(results)
    return results


def save_txt(result):
    with open("./data/5_spa1.txt", "a", encoding='utf-8') as fp:
        fp.write(str(result) + "\n")


def main():
    for i in range(1, 11):
        url = "https://spa1.scrape.center/api/movie/?limit=10&offset=0".format(i * 10)
        # time.sleep(random.randint(6,8))
        # print(url)
        html = crawel(url)
        results = parse_xpath(html)
        for item in results:
            save_txt(item)


main()
