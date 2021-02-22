# coding=utf-8
import requests
from fake_useragent import UserAgent
from lxml import etree
import random

requests.packages.urllib3.disable_warnings()


def crawel_zgcnews(url, headers, proxy):
    res = requests.get(url, headers=headers, verify=False,
                       timeout=15, proxies=proxy)
    # print(res.text)
    return res.text


def parse_news(html):
    tree = etree.HTML(html)
    # for i in range(1, 15):
    #     title_xpath = f'//*[@id="list - v - 1 "]/ul/li[{i}]/p/a'
    #     href_xpath = f'//*[@id="list-v-1"]/ul/li/p[{i}]/a/@href'
    #     title = tree.xpath(title_xpath)
    #     href = tree.xpath(href_xpath)
    href_xpath = '//*[@id="list-v-1"]/ul/li/p/a/@href'
    href_list = tree.xpath(href_xpath)
    print(href_list)
    return href_list


def crawel_zgcnews_content(href, headers, proxy):
    res = requests.get(href, headers=headers, verify=False,
                       timeout=15, proxies=proxy)
    # print(res.text)
    return res.text


def parse_content(html_content):
    tree = etree.HTML(html_content)
    # title_xpath = "/html/body/div[5]/div/div[1]/div[1]/h1"
    title_xpath = "//*[@class=\"article-header clearfix\"]/h1/text()"
    content_xpath = '//*[@id="article-content"]/div/p/text()'
    title = tree.xpath(title_xpath)
    print(title)
    content = tree.xpath(content_xpath)
    content_dict = {f'{title}': f'{content}'}
    return content_dict


def main(url, headers, proxy):
    content_list = []
    html = crawel_zgcnews(url, headers, proxy)
    href_list1 = parse_news(html)
    for href in href_list1:
        href = "http:" + str(href)
        html_content = crawel_zgcnews_content(href, headers, proxy)
        content_dict = parse_content(html_content)
        content_list.append(content_dict)
        print(content_list)


if __name__ == '__main__':
    url = "http://news.zol.com.cn/"
    # url = "http://www.baidu.com"
    user_agent = UserAgent()
    ua = user_agent.random
    headers = {
        "user_agent": ua
    }
    # proxy = {"http": "http://47.75.90.57:80"}
    proxy = {"http": "http://191.101.39.27:80"}
    # proxy = {"http": "http://191.101.39.154:80"}
    proxy_list = [{'http': 'http://39.100.18.200:8080'}, {'http': 'http://218.59.139.238:80'},
                  {'http': 'http://39.106.223.134:80'}, {'http': 'http://78.47.16.54:80'},
                  {'http': 'http://5.196.23.219:80'},
                  {'http': 'http://191.101.39.154:80'}, {'http': 'http://5.39.17.96:80'},
                  {'http': 'http://51.158.172.165:8811'}, {'http': 'http://152.67.24.187:80'},
                  {'http': 'http://161.35.4.201:80'}, {'http': 'http://205.141.197.38:8080'}]
    try:
        main(url, headers, proxy)
    except requests.exceptions.ProxyError:
        proxy = proxy_list[random.randint(0, len(proxy_list) - 1)]
        print(proxy)
        main(url, headers, proxy)
    # except Exception as e:
    #     print(e)
