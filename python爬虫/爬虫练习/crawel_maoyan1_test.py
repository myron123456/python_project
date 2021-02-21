import requests
from fake_useragent import UserAgent
import random
import re
import json
import pymysql
requests.packages.urllib3.disable_warnings()

user_agent = UserAgent()
ua = user_agent.random


# proxy = ""
def go_one_page(url):
    headers = {"User-Agent": ua}
    res = requests.get(url=url, headers=headers,verify=False,
                       timeout=15)
    if res.status_code == 200:
        result = res.text
        return result
    return None


def parse_one_page(html):
    content = """<i class="board-index board-index-\d+">(.*?)</i>[\s\S]*?<img data-src="([\S\s]*?)"[\s\S]*?<p class="name"><a [\S\s]*?">(.*?)</a></p>[\s\S]*?<p class="star">([\S\s]*?)</p>[\S\s]*?<p class="releasetime">(.*?)</p>[\S\s]*?<i class="integer">([\d\.]+)</i><i class="fraction">(\d+)<\/i>"""
    items = re.findall(content, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip(),
            'time': item[4].strip(),
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result1.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def write_to_mysql(item):
    # 数据库名称和密码
    name = 'root'
    password = 'myron123'  # 替换为自己的用户名和密码
    # 建立本地数据库连接(需要先开启数据库服务)
    db = "mvs"
    db = pymysql.connect('localhost', name, password, db, charset='utf8')
    cursor = db.cursor()
    txt = item
    id = txt['index']
    image = txt['image']
    title = txt['title']
    actor = txt['actor'].replace(",", " ")
    time = txt['time']
    score = txt['score']
    sql = 'insert into my_100 (id,image,title,actor,time,score) values("{}","{}","{}","{}","{}","{}")'.format(
        id, image, title, actor, time, score)
    cursor.execute(sql)
    print('插入成功')
    db.commit()


def main(offset):
    url = "https://ssr1.scrape.center/page/{}".format(str(offset))
    html = go_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        print(type(item))
        write_to_file(item)
        # write_to_mysql(item)
    # print(html)

if __name__ == '__main__':
    for i in range(1,11):
        main(i)