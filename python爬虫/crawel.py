import requests
import re
import time
import json
import pymysql
import os


def go_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    }
    proxy_list = {
        "http": "36.248.132.25:9999",
        "http": "175.42.122.236:9999",
        "http": "49.89.84.158:9999",
        "http": "175.42.129.42:9999",
        "http": "117.69.153.114:9999",
        "http": "112.91.78.181:9999",
        "http": "120.83.105.95:9999",
        "http": "39.108.59.34:8118",
        "http": "112.111.217.160:9999",
    }
    res = requests.get(url=url, headers=headers, timeout=15, proxies=proxy_list)
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
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def write_to_mysql(content):
    # 数据库名称和密码
    name = 'root'
    password = ' '  # 替换为自己的用户名和密码
    # 建立本地数据库连接(需要先开启数据库服务)
    db = "mvs"
    db = pymysql.connect('localhost', name, password, db, charset='utf8')
    cursor = db.cursor()
    # sqlSentence = "use mvs"
    # cursor.execute(sqlSentence)
    sql = 'insert into maoyan_top100 values(%s,%s,%s,%s,%s)'
    cursor.executemany(sql, content)


def main(offset):
    url = "https://maoyan.com/board/4?offset={}".format(str(offset))
    html = go_one_page(url)
    for item in parse_one_page(html):
        print(item)
        # write_to_file(item)
        write_to_mysql(item)
    # print(html)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(5)
