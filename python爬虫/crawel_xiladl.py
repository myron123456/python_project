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
    # proxy = {"HTTP": "52.149.152.236:80"}
    res = requests.get(url, headers=headers, verify=False,
                       allow_redirects=False, timeout=15)
    if res.status_code == 200:
        return res.text
    return None


def parse_one_page(html):
    pattern = "<tr>[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>(.*?)</td>"
    items = re.findall(pattern, html)
    for item in items:
        item = list(item)
        if item[1] == "HTTP代理":
            item[1] = "http"
        elif item[1] == "HTTPS代理" or item[1] == "HTTP,HTTPS代理":
            item[1] = "https"
        yield {
            # 'type': item[1],
            # 'target': item[0]
            "{}".format(item[1]): "{}".format(str(item[1])+"://"+str(item[0]))
        }


def verify(content):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
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
    with open('xila_dl.txt', 'a', encoding='utf-8') as f:
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
    sql = 'insert into xila_dl(target) values("{}")'.format(target)
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
    sql = 'insert into xila_ndl(target) values("{}")'.format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()


def main():
    # xila free proxy IP,页面1的url特殊
    for i in range(1, 11):
        try:
            if i==1:
                url = "http://www.xiladaili.com/gaoni/"
            else:
                url = "http://www.xiladaili.com/gaoni/{}/".format(str(i))
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
