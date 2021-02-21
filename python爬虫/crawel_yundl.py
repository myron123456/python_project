import json
import re
import time
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
        main()
        # 释放锁，开启下一个线程
        threadLock.release()


def crawel_one_page(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Connection': 'close'
    }
    # proxy = {'http': 'http://220.174.236.211:8091'}
    res = requests.get(url, headers=headers, verify=False,
                       allow_redirects=False, timeout=15)
    print(url)
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
            item[2] = "http"
        yield {
            # 'type': item[2],
            # 'target': str(item[0])+":"+str(item[1])
            "{}".format(item[2]): "{}".format(str(item[2])+"://"+str(item[0]) + ":" + str(item[1]))
        }


def verify(content):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
        }
        url2 = "http://httpbin.org/get"
        url3 = "https://httpbin.org/get"
        if "https" in str(content):
            url = url3
        else:
            url = url2
        p = requests.get(url=url, headers=headers, proxies=content, timeout=15)
        print(p.text)
        # time.sleep(2.3)
        # print(content)
        item = list(content.items())[0]
        item = {'{}'.format(item[0]): '{}'.format(item[1])}
        print(item)
        tg = list(item.values())[0].split(':')[1][2:].split('.')
        # tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
        tg = str(tg[0]) + "." + str(tg[1])
        if p.status_code == 200:
            # print(item)
            write_to_mysql1(item)
            if tg in p.text.strip():
                print("gn ok")
                write_to_mysql2(item)
    except  Exception as e:
        print(e)


def write_to_txt(item):
    with open('yun_dl.txt', 'a', encoding='utf-8') as f:
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
    sql = 'insert into yun_dl(target) values("{}")'.format(target)
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
    sql = 'insert into yun_ndl(target) values("{}")'.format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()


def main():
        # j用来控制爬取网站标注的高匿和普通匿名代理，1为高匿，2为普通匿名
        for j in range(1,3):
            # 此站点仅开放100条，7页
            for i in range(1, 8):
                try:
                    url = "http://www.ip3366.net/free/?stype={}&page={}".format(str(j),str(i))
                    # time.sleep(3.6)
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

# main()
