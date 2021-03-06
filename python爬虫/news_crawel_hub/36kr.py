import pymysql
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
import json

requests.packages.urllib3.disable_warnings()

global result_list
result_list = []


def crawel_kuaixun1(url):
    user_agent = UserAgent()
    ua = user_agent.random
    headers = {
        "User-Agent": ua,
        "Refer": "https://www.36kr.com/",
    }
    # proxy = {'http': 'http://112.246.233.201:8060'}
    proxy = {"http": "http://5.39.17.96:80"}
    res = requests.get(url=url, headers=headers, verify=False, timeout=15)
    # print(res.text)
    return res.text


def parse_news(html):
    tree = etree.HTML(html)
    for i in range(1, 11):
        # title_path = "//*[@id=\"app\"]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/div[1]/div[" + str(
        #     i) + "]/div[2]/div/a/text()"
        # content_path = "//*[@id=\"app\"]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/div[1]/div[" + str(
        #     i) + "]/div[2]/div/div[2]/span/text()"
        title_path = "//a[@class=\"item-title\"]/text()"
        content_path = "//div[@class=\"item-desc\"]/span/text()"

        news_title = tree.xpath(title_path)[i]
        # print(news_title)
        # news_title = str(news_title).replace('“', '\"').replace('”', '\"')
        news_content = tree.xpath(content_path)[i]
        # print(news_content)
        # news_content = str(news_content).replace('“', '\"').replace('”', '\"')
        news_dict = {f"{news_title}": f"{news_content}"}
        global result_list
        result_list.append(news_dict)
        # print(news_titles)
        # for news_title in news_titles:
        #     # print(news_title)
        #     result_list.append(news_title)
        # return result_list
    pattern = '\"pageCallback\":\"(.*?)\"'
    pageCallback = re.findall(pattern, html)
    return result_list, pageCallback


def crawel_kuaixun2(url, post_data):
    user_agent = UserAgent()
    ua = user_agent.random
    headers = {
        "User-Agent": ua,
        "Refer": "https://www.36kr.com/",
        'content-type': 'application/json',
    }
    # proxy = {'http': 'http://112.246.233.201:8060'}
    proxy = {"http": "http://5.39.17.96:80"}
    data = '{"partner_id":"web","timestamp":1613897745666,"param":{"pageSize":20,"pageEvent":1,"pageCallback":"' + post_data + '","siteId":1,"platformId":2}}'
    res = requests.post(url=url, data=data, headers=headers, verify=False, timeout=15)
    # print(res.text)
    return res.text


def parse_news2(html):
    html = json.loads(html)
    for i in range(1, 20):
        news_title = html['data']['itemList'][i]['templateMaterial']['widgetTitle']
        # news_title=str(news_title).replace('“','\"').replace('”','\"')
        news_content = html['data']['itemList'][i]['templateMaterial']['widgetContent']
        # news_content = str(news_content).replace('“', '\"').replace('”', '\"')
        news_dict = {f"{news_title}": f"{news_content}"}
        # global result_list
        result_list.append(news_dict)
    # result_list = result_list[:-1]
    pageCallback = html['data']['pageCallback']
    return result_list, pageCallback


def write_to_txt(news):
    with open("36kr_news.txt", 'a', encoding='utf-8') as f:
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
    sql = 'insert into news_hub(refer,title,content) values("{}","{}","{}")'.format("来源：36kr",title,content)
    cursor.execute(sql)
    print('插入成功')
    db.commit()

def main():
    max_page = 4
    url = "https://36kr.com/newsflashes"
    html = crawel_kuaixun1(url)
    newslist = parse_news(html)
    newspage = newslist[0]
    # print(newspage)
    url2 = "https://gateway.36kr.com/api/mis/nav/newsflash/flow"
    post_data = newslist[1][0]
    for i in range(1, max_page + 1):
        global result_list
        news_data = crawel_kuaixun2(url2, post_data)
        parse_data2 = parse_news2(news_data)
        post_data = parse_data2[1]
        # print(parse_data2[0])
        result_list.append(parse_data2[0])
        result_list = result_list[:-1]
    # print("1111", result_list)
    # print(result_list_parse)
    for news in result_list:
        write_to_txt(news)
        # print("------------",news)
        for i in news:
            title = i
            content = news[f'{title}']
            # print(title)
        # for j in news:
        #     content = j
        #     print(content)
        # title = news.keys()
        # content = news.values()
        write_to_mysql(title,content)
        # print(parse_data2)

    print(result_list)
    print(len(result_list))


main()
