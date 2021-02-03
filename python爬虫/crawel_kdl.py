import requests
import random
import re
import time
import json
import pymysql

requests.packages.urllib3.disable_warnings()


# proxy = {"http": "52.149.152.236:80"}
# url = "http://httpbin.org/get"
# # res = requests.get(url=url, proxies=proxy, timeout=10)
# p = requests.get('http://icanhazip.com', proxies=proxy)
# print(p.text)

# proxy_list=[]

# 尝试代理agents增强反反爬


def random_agent(self):
    user_agents = [
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
        "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
        "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
    ]
    return random.choice(user_agents)


def crawel_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    }
    # proxy = {"http": "http://52.149.152.236:80"}
    res = requests.get(url, headers=headers, verify=False,
                       allow_redirects=False, timeout=15)
    if res.status_code == 200:
        return res.text
    return None


def re_parse_one_page(html):
    # result_list = []
    content = """<td data-title="IP">(.*?)</td>[\s\S]*?<td data-title="PORT">(.*?)</td>[\S\s]*?<td data-title="类型">(.*?)</td>"""
    # list_contents = re.findall(content, html)
    # for list_content in list_contents:
    #     print(list_content)
    #     result_type = list_content[2]
    #     result_url = str(list_content[0]) + ":" + str(list_content[1])
    #     result = '"{}": "{}"'.format(result_type, result_url)
    #     json_str = '{}'.format(result_type) + ":" + '{}'.format(result_url)
    #     print(json_str)
    #     result_list.append(json_str)
    # return result_list
    items = re.findall(content, html)
    for item in items:
        item = list(item)
        if item[2] == "HTTP":
            item[2] = "http"
        else:
            item[2]="https"
        yield {
            # 'type': item[2],
            # 'target': str(item[0])+":"+str(item[1])
            "{}".format(item[2]): "{}".format(str(item[2])+"://"+str(item[0]) + ":" + str(item[1]))
        }


def verify(content):
    try:
        p = requests.get('http://icanhazip.com', proxies=content, timeout=10)
        print(p.text)
        time.sleep(2.5)
        item = list(content.items())[0]
        item = {'{}'.format(item[0]): '{}'.format(item[1])}
        tg = list(item.values())[0].split(':')[1][2:].split('.')
        tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
        print(tg)
        if p.status_code == 200:
            write_to_mysql1(item)
            if tg in p.text.strip():
                print("gn ok")
                write_to_mysql2(item)
    except  Exception as e:
        print(e)


def write_to_txt(item):
    with open('kdl.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def write_to_mysql1(target):
    # # 数据库名称和密码
    # user = 'root'
    # passwd = 'myron123'  # 替换为自己的用户名和密码
    # # 建立本地数据库连接(需要先开启数据库服务)
    # host="localhost"
    # port = 3306
    # db = "crawel"
    # db = pymysql.connect(user,passwd,host,port,db)
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='crawel'
    )
    cursor = db.cursor()
    sql = 'insert into dl(target) values("{}")'.format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()


def write_to_mysql2(target):
    # # 数据库名称和密码
    # name = 'root'
    # password = 'myron123'  # 替换为自己的用户名和密码
    # # 建立本地数据库连接(需要先开启数据库服务)
    # host = "localhost"
    # db = "crawel"
    # port = 3306
    # db = pymysql.connect(host,port,name,  password, db, charset='utf8')
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='crawel'
    )
    cursor = db.cursor()
    sql = 'insert into ndl(target) values("{}")'.format(target)
    cursor.execute(sql)
    print('插入高匿成功')
    db.commit()


def main():
        for i in range(1, 11):
            try:
                url = "https://www.kuaidaili.com/free/inha/{}/".format(str(i))
                time.sleep(5.5)
                html = crawel_one_page(url)
                # f = re_parse_one_page(html)
                # print(f)
                for item in re_parse_one_page(html):
                    # target = verify(item)
                    # write_to_mysql(target)
                    print(item)
                    verify(item)
            except Exception as e:
                print(e)


main()
