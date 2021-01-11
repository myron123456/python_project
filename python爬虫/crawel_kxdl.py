import json
import re
import time
import pymysql
import requests

requests.packages.urllib3.disable_warnings()


def crawel_one_page(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Connection': 'close'
    }
    # proxy = {"http": "http://52.149.152.236:80"}
    res = requests.get(url, headers=headers, verify=False,
                       allow_redirects=False, timeout=15)
    if res.status_code == 200:
        return res.text
    return None


def parse_one_page(html):
    pattern = "<tr.*?>[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>.*?</td>[\s\S]*?<td>(.*?)</td>"
    items = re.findall(pattern, html)
    for item in items:
        item = list(item)
        if item[2] == "HTTP,HTTPS" or item[2] == "HTTPS":
            item[2] = "https"
        elif item[2] == "HTTP":
            item[2]="http"
        yield {
            # 'type': item[2],
            # 'target': str(item[0])+":"+str(item[1])
            "{}".format(item[2]): "{}".format(str(item[2])+"://"+str(item[0]) + ":" + str(item[1]))
        }


def verify(content):
    try:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        }
        p = requests.get('http://icanhazip.com', headers=headers, proxies=content, timeout=10)
        print(p.text)
        time.sleep(2.3)
        # print(content)
        item = list(content.items())[0]
        item = {'{}'.format(item[0]): '{}'.format(item[1])}
        print(item)
        tg = list(item.values())[0].split(':')[1][2:].split('.')
        tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
        if p.status_code == 200:
            # print(item)
            write_to_mysql1(item)
            if tg in p.text.strip():
                print("gn ok")
                write_to_mysql2(item)
    except  Exception as e:
        print(e)


def write_to_txt(item):
    with open('xiaohuan_dl_http.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        # f.write(str(item)+'\n')

def write_to_mysql1(target):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='crawel'
    )
    cursor = db.cursor()
    sql = 'insert into kaixin_dl(target) values("{}")'.format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()


def write_to_mysql2(target):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='crawel'
    )
    cursor = db.cursor()
    sql = 'insert into kaixin_ndl(target) values("{}")'.format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()


def main():
    # j用来控制爬取网站标注的高匿和普通匿名代理，1为高匿，2为普通匿名
    for j in range(1,3):
        for i in range(1, 11):
            try:
                url = "http://www.kxdaili.com/dailiip/{}/{}.html".format(str(j),str(i))
                time.sleep(3.6)
                html = crawel_one_page(url)
                if html is not None:
                    for content in parse_one_page(html):
                        # print(content)
                        # write_to_txt(content)
                        verify(content)
                else:
                    print("访问目标网站失败")
            except Exception as e:
                print(e)


main()
