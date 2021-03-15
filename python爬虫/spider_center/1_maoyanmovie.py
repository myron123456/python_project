# -*- codeing=utf-8 -*-
# @Time:2021/3/15 14:22
# @Author:
# @File:1_maoyanmovie.py.py
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
    html = etree.HTML(html)
    title_xpath = "//h2[@class=\"m-b-sm\"]/text()"
    score_xpath = "//p[@class=\"score m-t-md m-b-n-sm\"]/text()"
    # type_xpath = "//div[@class=\"categories\"]//span/text()"
    for i in range(0, 10):
        result_dict = {}  # 注意字典的位置
        type_xpath = f"//div[@class=\"el-col el-col-18 el-col-offset-3\"]/div[{i + 1}]//div[@class=\"categories\"]//span/text()"
        result_dict['title'] = html.xpath(title_xpath)[i]
        result_dict['score'] = str(html.xpath(score_xpath)[i]).strip()
        result_dict['type'] = ";".join(html.xpath(type_xpath))
        print(result_dict)
        # print(result_dict['type'])
        results.append(result_dict)
    # print(results)
    return results


def save_txt(result):
    with open("./data/1_maoyan.txt", "a", encoding='utf-8') as fp:
        fp.write(str(result) + "\n")


def main():
    results_list = []
    for i in range(1, 11):
        url = "https://ssr1.scrape.center/page/{}".format(i)
        # time.sleep(random.randint(3,5))
        # print(url)
        html = crawel(url)
        results = parse_xpath(html)
        for item in results:
            save_txt(item)


main()
