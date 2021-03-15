import json

import pymysql
import requests
import threading

requests.packages.urllib3.disable_warnings()


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        proxy_list_plus()
        # 释放锁，开启下一个线程
        threadLock.release()


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
    # sql = "select distinct target from xila_ndl;"
    sql = "select distinct target from proxies1;"
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


def write_to_txt(item):
    with open('xila_ndl.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        # f.write(str(item)+    '\n')
def write_to_mysql(target):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='crawel'
    )
    cursor = db.cursor()
    # sql = 'insert into proxy(target) values("{}")'.format(target)
    sql = 'insert into proxies2(target) values("{}")'.format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()

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
            url1 = 'http://icanhazip.com'
            url2 = "http://httpbin.org/get"
            url3 = "https://httpbin.org/get"
            if "https" in str(proxy):
                url = url3
            else:
                url = url2
            print("================== 第" + str(i) + "次尝试==========")
            global p
            p = requests.get(url=url, headers=headers, proxies=proxy, verify=False, allow_redirects=False, timeout=10)
            # print(p.text)
            item = list(proxy.items())[0]
            item = {'{}'.format(item[0]): '{}'.format(item[1])}
            result = json.loads(p.text)['origin']
            if p.status_code == 200 or "Backend not available" in p.text or "" in p.text or "html" in p.text:
                tg = list(proxy.values())[0].split(':')[1][2:].split('.')
                tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
                if tg in result.strip():
                    proxy_list.append(item)
                    write_to_txt(item)
                    write_to_mysql(item)
            print(proxy_list)
        except Exception as e:
            print(e)

    return proxy_list


# proxy_list_plus()
threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 4)
thread5 = myThread(5, "Thread-5", 5)
thread6 = myThread(6, "Thread-6", 6)
thread7 = myThread(7, "Thread-7", 7)
thread8 = myThread(8, "Thread-8", 8)
# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)
threads.append(thread6)
threads.append(thread7)
threads.append(thread8)
# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")

# print(proxy_list())
# def write_to_proxy_txt():
#     proxys = read_proxys()
#     for i in range(0,len(proxys)-1):
#         proxy = proxys[i][0]
#         with open('proxys.txt','a') as f:
#             f.write(proxy+"\n")
# write_to_proxy_txt()

# proxy_list = [{'http': 'http://47.57.124.95:80'}, {'http': 'http://39.100.18.200:8080'},
#               {'http': 'http://218.59.139.238:80'}, {'http': 'http://180.250.12.10:80'},
#               {'http': 'http://203.198.94.132:80'}, {'http': 'http://39.106.223.134:80'},
#               {'http': 'http://91.205.174.26:80'}, {'http': 'http://89.187.177.91:80'},
#               {'http': 'http://112.245.17.202:8080'}, {'http': 'http://95.213.144.199:80'},
#               {'http': 'http://210.212.253.227:8080'}, {'http': 'http://8.210.120.182:8080'},
#               {'http': 'http://52.149.152.236:80'}, {'http': 'http://47.106.162.218:80'},
#               {'http': 'http://89.187.177.105:80'}, {'http': 'http://89.187.177.97:80'},
#               {'http': 'http://5.196.23.219:80'}, {'http': 'http://89.187.177.92:80'},
#               {'http': 'http://106.14.198.6:8080'}, {'http': 'http://47.75.90.57:80'},
#               {'http': 'http://39.108.230.67:8080'}, {'http': 'http://182.140.244.163:8118'}]
# print(len(proxy_list))
