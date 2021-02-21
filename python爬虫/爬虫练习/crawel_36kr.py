import json
import re
import time
import pymysql
import requests
requests.packages.urllib3.disable_warnings()

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
proxy_list_bak = []
def proxy_list():
    proxys = read_proxys()
    proxy_list = []
    for i in range(0,len(proxys)-1):
        try:
            proxy = proxys[i][0]
            proxy = eval(proxy)
            print(proxy)
            headers = {
                "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            }
            time.sleep(2.5)
            p = requests.get('http://icanhazip.com', headers=headers, proxies=proxy, timeout=30)
            if p.status_code == 200:
                proxy = {'{}'.format(proxy[0]): '{}'.format(proxy[1])}
                print(proxy)
                tg = list(proxy.values())[0].split(':')[1][2:].split('.')
                tg = str(tg[0]) + "." + str(tg[1]) + "." + str(tg[2])
                print(tg)
                if tg in p.text.strip():
                    proxy_list.append(proxy)
                    proxy_list_bak.append(proxy)
            print(proxy_list)
        except Exception as e:
            print(e)
    return proxy_list
# print(proxy_list())

def crawel_one_page(url):
    proxy = {'http': 'http://51.158.186.242:8811'}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Connection': 'close'
    }
    res = requests.get(url, headers=headers, verify=False,
                       allow_redirects=False, timeout=15,proxies =proxy)
    if res.status_code == 200:
        print(res.headers['location'])
        return res.text
    return None
def parse_one_page():
    pass
def main():
    url = "https://36kr.com/newsflashes"
    html = crawel_one_page(url)
    print(html)
    # if html is not None:
    #     for content in parse_one_page(html):

main()