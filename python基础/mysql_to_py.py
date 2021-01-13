import pymysql
import requests


# import pandas as pd
def read_proxys():
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="myron123",
        database="crawel",
    )
    cursor = db.cursor()
    sql = "select distinct target from proxy;"
    cursor.execute(sql)
    proxys = cursor.fetchall()
    db.commit()
    return proxys


def proxy_list():
    proxys = read_proxys()
    proxy_list = []
    for i in range(0, len(proxys) - 1):
        proxy = proxys[i][0]
        proxy = eval(proxy)
        proxy_list.append(proxy)


def proxy_list_plus():
    proxys = read_proxys()
    proxy_list = []
    for i in range(0, len(proxys) - 1):
        try:
            proxy = proxys[i][0]
            proxy = eval(proxy)
            headers = {
                "User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
            }
            p = requests.get('http://icanhazip.com', headers=headers, proxies=proxy, timeout=10)
            if p.status_code == 200:
                tg = list(proxy.values())[0].split(':')[1][2:].split('.')
                tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
                if tg in p.text.strip():
                    proxy_list.append(proxy)
            # print(proxy_list)
        except Exception as e:
            print(e)
    return proxy_list


# print(proxy_list())
# def write_to_proxy_txt():
#     proxys = read_proxys()
#     for i in range(0,len(proxys)-1):
#         proxy = proxys[i][0]
#         with open('proxys.txt','a') as f:
#             f.write(proxy+"\n")
# write_to_proxy_txt()

proxy_list = [{'http': 'http://47.57.124.95:80'}, {'http': 'http://39.100.18.200:8080'},
              {'http': 'http://218.59.139.238:80'}, {'http': 'http://180.250.12.10:80'},
              {'http': 'http://203.198.94.132:80'}, {'http': 'http://39.106.223.134:80'},
              {'http': 'http://91.205.174.26:80'}, {'http': 'http://89.187.177.91:80'},
              {'http': 'http://112.245.17.202:8080'}, {'http': 'http://95.213.144.199:80'},
              {'http': 'http://210.212.253.227:8080'}, {'http': 'http://8.210.120.182:8080'},
              {'http': 'http://52.149.152.236:80'}, {'http': 'http://47.106.162.218:80'},
              {'http': 'http://89.187.177.105:80'}, {'http': 'http://89.187.177.97:80'},
              {'http': 'http://5.196.23.219:80'}, {'http': 'http://89.187.177.92:80'},
              {'http': 'http://106.14.198.6:8080'}, {'http': 'http://47.75.90.57:80'},
              {'http': 'http://39.108.230.67:8080'}, {'http': 'http://182.140.244.163:8118'}]
print(len(proxy_list))
