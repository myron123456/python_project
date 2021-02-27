# coding=utf-8
import json

import pymysql
import requests
from fake_useragent import UserAgent
from lxml import etree
import random

requests.packages.urllib3.disable_warnings()


def crawel_tmtpost(url, headers, proxy):
    try:
        res = requests.get(url, headers=headers, verify=False,
                           timeout=15)
        return res.text
    except Exception as e:
        print(e)
        return None
    # print(res.text)


def parse_news(html):
    tree = etree.HTML(html)
    # for i in range(1, 15):
    #     title_xpath = f'//*[@id="list - v - 1 "]/ul/li[{i}]/p/a'
    #     href_xpath = f'//*[@id="list-v-1"]/ul/li/p[{i}]/a/@href'
    #     title = tree.xpath(title_xpath)
    #     href = tree.xpath(href_xpath)
    # href_xpath = '//li[@data-time="昨天"]/a/@href'
    # href_xpath = '//a[@target="_blank"]/@href'
    href_xpath = '//ul[@class="word_list"]/li/a/@href'
    href_list = tree.xpath(href_xpath)
    print(href_list)
    return href_list


def crawel_tmtpost_content(href, headers, proxy):
    try:
        res = requests.get(href, headers=headers, verify=False,
                           timeout=15)
        return res.text
    except Exception as e:
        print(e)
        # print(res.text)
        return None


def parse_content(html_content):
    tree = etree.HTML(html_content)
    # title_xpath = "/html/body/div[7]/section/div[1]/h2/text()"
    # content_xpath = '/html/body/div[7]/section/div[1]/div[1]/pre/text()'
    title_xpath = "//h2[@class=\"title\"]/text()"
    content_xpath = "//div[@class=\"main\"]/pre/text()"
    title = tree.xpath(title_xpath)[0]
    # print(title)
    content = tree.xpath(content_xpath)[0]
    content = str(content).replace("\n", "")
    content_dict = {f'{title}': f'{content}'}
    return content_dict


def write_to_txt(news):
    with open("tmtpost_news.txt", 'a', encoding='utf-8') as f:
        f.write(str(news) + "\n")

def write_to_mysql(title,content):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='news_data'
    )
    cursor = db.cursor()
    sql = 'insert into news_hub(refer,title,content) values("{}","{}","{}")'.format("来源：钛媒体",title,content)
    cursor.execute(sql)
    print('插入成功')
    db.commit()

def main(url, headers, proxy):
    content_list = []
    html = crawel_tmtpost(url, headers, proxy)
    if html is not None:
        href_list1 = parse_news(html)
        for href in href_list1:
            if href.startswith('/nictation'):
                href = "http://www.tmtpost.com" + str(href)
                # print(href)
                html_content = crawel_tmtpost_content(href, headers, proxy)
                # print(html_content)
                if html_content is not None:
                    content_dict = parse_content(html_content)
                    write_to_txt(content_dict)
                    for i in content_dict:
                        title = i.replace("\\n", "").replace("\\", "")
                        content = content_dict[f'{title}'].replace("\\n", "").replace("\\", "")
                        write_to_mysql(title, content)
                    content_list.append(content_dict)

                print(content_list)


if __name__ == '__main__':
    url = "https://www.tmtpost.com/nictation"
    user_agent = UserAgent()
    ua = user_agent.random
    headers = {
        "user_agent": ua
    }
    # proxy = {"http": "http://47.75.90.57:80"}
    # proxy = {"http": "http://191.101.39.27:80"}
    # proxy = {"http": "http://191.101.39.154:80"}
    proxy = {"http": "http://139.99.105.185:80"}
    # proxy = {"http": "http://52.19.94.82:33128"}
    # proxy = {"http": "http://124.41.240.203:55948"}
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
