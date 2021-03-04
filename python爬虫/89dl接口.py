import json
import pymysql
import requests

requests.packages.urllib3.disable_warnings()


def write_to_mysql1(target):
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
    print('插入成功')
    db.commit()


def verify():
    with open("xiaohuan_dl_http.txt", 'r') as f:
        for ip in f.readlines():
            try:
                ip = ip.replace('\n', '')
                print(ip)
                url = "http://icanhazip.com"
                headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                           }
                content = {'http': 'http://{}'.format(ip)}
                headers = {
                    "User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
                    ,
                }
                url1 = 'http://icanhazip.com'
                url2 = "http://httpbin.org/get"
                url3 = "https://httpbin.org/get"
                if "https" in str(content):
                    url = url3
                else:
                    url = url2
                p = requests.get(url=url, headers=headers, proxies=content, verify=False, allow_redirects=False,
                                 timeout=5)
                # print(p.text)
                if p.status_code == 200:
                    # print(item)
                    result = json.loads(p.text)['origin']
                    # time.sleep(0.3)
                    # print(content)
                    item = list(content.items())[0]
                    item = {'{}'.format(item[0]): '{}'.format(item[1])}
                    print(item)
                    tg = list(item.values())[0].split(':')[1][2:].split('.')
                    # tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
                    tg = str(tg[0]) + "." + str(tg[1])
                    write_to_mysql1(item)
                    # if tg in p.text.strip():
                    if tg in result.strip() or "Backend not available" in p.text or "<html>" in p.text or "" in p.text:
                        print("gn ok")
                        write_to_mysql2(item)
            # except "Expecting value: line 1 column 1 (char 0)":
            #     print("==============特殊代理===================")
            #     write_to_mysql2(item)
            except  Exception as e:
                print(e)


verify()
