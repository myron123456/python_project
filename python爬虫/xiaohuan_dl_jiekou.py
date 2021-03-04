import requests
import pymysql
import time
def write_to_mysql1(target):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='crawel'
    )
    cursor = db.cursor()
    sql = 'insert into xiaohuan_dl(target) values("{}")'.format(target)
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
    sql = 'insert into xiaohuan_ndl(target) values("{}")'.format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()

# with open("xiaohuan_dl_http.txt",'r') as f:
#         for ip in f.readlines():
#             try:
#                 ip = ip.replace('\n','')
#                 print(ip)
#                 url = "http://icanhazip.com"
#                 headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#                            }
#                 proxy = {'http': 'http://{}'.format(ip)}
#                 # proxy = {'https': 'https://{}'.format(ip)}
#                 print(proxy)
#                 res = requests.get(url=url, headers=headers, verify=False,
#                                    allow_redirects=False, timeout=15,proxies=proxy)
#                 # time.sleep(3)
#                 print(proxy)
#                 item = list(proxy.items())[0]
#                 item = {'{}'.format(item[0]): '{}'.format(item[1])}
#                 print(item)
#                 tg = list(item.values())[0].split(':')[1][2:].split('.')
#                 tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
#                 print(tg)
#                 if res.status_code == 200:
#                     # print(item)
#                     write_to_mysql1(item)
#                     if tg in res.text.strip():
#                         print("gn ok")
#                         write_to_mysql2(item)
#             except Exception as e:
#                 print(e)

with open("xiaohuan_dl_https.txt", 'r') as f:
    for ip in f.readlines():
        try:
            ip = ip.replace('\n', '')
            print(ip)
            url = "http://icanhazip.com"
            headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                       }
            proxy = {'http': 'http://{}'.format(ip)}
            # proxy = {'https': 'https://{}'.format(ip)}
            print(proxy)
            res = requests.get(url=url, headers=headers, verify=False,
                               allow_redirects=False, timeout=5, proxies=proxy)
            # time.sleep(3)
            print(res.text)
            item = list(proxy.items())[0]
            item = {'{}'.format(item[0]): '{}'.format(item[1])}
            print(item)
            tg = list(item.values())[0].split(':')[1][2:].split('.')
            tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
            print(tg)
            if res.status_code == 200:
                # print(item)
                write_to_mysql1(item)
                if tg in res.text.strip():
                    print("gn ok")
                    write_to_mysql2(item)
        except Exception as e:
            print(e)