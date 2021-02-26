# coding=utf-8
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
    proxy = {"http": "http://89.221.223.234:80"}
    res = requests.get(url=url, headers=headers, verify=False, proxies=proxy, timeout=15)
    return res.text


def crawel_ribang_content(url):
    user_agent = UserAgent()
    ua = user_agent.random
    headers = {
        "User-Agent": ua,
    }
    # proxy = {'http': 'http://112.246.233.201:8060'}
    proxy = {"http": "http://89.221.223.234:80"}
    res = requests.get(url=url, headers=headers, verify=False, proxies=proxy, timeout=15)
    htmls = res.text
    tree = etree.HTML(htmls)
    # print(tree)
    ### xpath中/text()不要丢
    # 为什么完整xpath提取到的为空？
    # title_xpath = "/html/body/div[5]/div[1]/h1/text()"
    # content_xpath = "/html/body/div[5]/div[1]/div[3]/text()"
    title_xpath = '//*[@id="dt"]/div[1]/h1/text()'
    content_xpath = '//*[@id="paragraph"]/p/text()'
    news_title = tree.xpath(title_xpath)[0]
    print(news_title)
    news_content = tree.xpath(content_xpath)
    news_dict = {f"{news_title}": f"{news_content}"}
    print(news_dict)
    global result_list
    result_list.append(news_dict)
    return result_list


def parse_news(html):
    href_list = []
    for i in range(1, 11):
        href_path = "/html/body/ul[2]/li[{}]/a/@href".format(i)
        # 此处若是使用html就会报错，局部变量对全局变量产生冲突
        htmls = etree.HTML(html)
        # print(html)
        href = htmls.xpath(href_path)[0]
        # print(href)
        href_list.append(href)
        print(href_list)
    return href_list


def write_to_txt(news):
    with open("ithome_news.txt", 'a', encoding='utf-8') as f:
        f.write(str(news) + "\n")


def main():
    # url = "https://www.ithome.com"
    global result_list
    url = "https://www.ithome.com/block/rank.html"
    html = crawel_ribang(url)
    # print(html)
    href_list = parse_news(html)[2:]
    for href in href_list:
        result_list = crawel_ribang_content(href)
        for news in result_list:
            write_to_txt(news)
    print(result_list)


main()
