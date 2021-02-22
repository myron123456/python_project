import requests
import re
import time
import json
import pymysql
import os
import json
from fake_useragent import UserAgent
user_agent = UserAgent()
ua = user_agent.random

def go_one_page(url):
    headers = {
        "User-Agent": ua,
    }
    proxy_list = {
        "http": "175.42.129.42:9999",
        "http": "117.69.153.114:9999",
        "http": "112.91.78.181:9999",
        "http": "120.83.105.95:9999",
        "http": "39.108.59.34:8118",
        "http": "112.111.217.160:9999",
        "http": "182.46.112.205:9999",
        "http": "115.221.240.127:9999",
        "http": "113.194.28.38:9999",
        "http": "183.166.70.63:9999",
        "http": "103.216.82.18:6666",
        "http": "112.250.107.37:53281",
        "http": "31.172.105.144:8080",
        "http": "190.57.143.66:50719",
        "http": "140.238.229.21:80",
        "http": "197.211.238.220:54675",
        "http": "186.225.63.241:8080",
        "http": "171.35.163.64:9999",
        "http": "122.5.107.206:9999",
        "http": "5.16.0.169:8080",
        "http": "185.128.37.4:8080",
        "http": "103.36.11.240:14571",
        "http": "103.39.49.10:80",
        "http": "110.243.5.18:9999",
        "http": "5.141.244.97:61288",
        "http": "180.183.246.110:8080",
        "http": "103.148.210.110:8080",
        "http": "117.247.190.141:80",
        "http": "165.22.64.68:43323",
        "http": "34.64.114.171:80",
        "http": "183.166.20.171:9999",
        "http": "175.146.208.20:9999",
        "http": "113.195.153.168:9999",
        "http": "114.99.161.210:20132",
        "http": "114.249.113.35:9000",
        "http": "182.23.52.114:6060",
        "http": "171.35.148.184:9999",
        "http": "182.46.207.97:9999",
        "http": "45.4.85.75:9991",
        "http": "182.46.123.225:9999",

    }
    # proxy = {'http': 'http://171.35.149.45:9999'}
    # proxy = {'https': 'https://49.89.67.177:9999'}
    res = requests.get(url=url, headers=headers,
                       timeout=15)
    if res.status_code == 200:
        result = res.text
        # content = "<p class=\"name\"><a .*?>(.*?)<\/a><\/p>"
        #         content = ''' <p class="name"><a .*?>(.*?)</a></p>
        #         <p class="star">
        #                 (.*?)
        #         </p>
        # <p class="releasetime">(.*?)</p>    </div>'''
        # //*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a
        return result
    return None


# url ="https://maoyan.com/board/4?offset=20"
# html=go_one_page(url)
# print(html)


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
    url = "https://maoyan.com/board/4?offset={}".format(str(offset))
    html = go_one_page(url)
    print(html)
    for item in parse_one_page(html):
        print(item)
        print(type(item))
        # write_to_file(item)
        write_to_mysql(item)
    # print(html)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(5)
