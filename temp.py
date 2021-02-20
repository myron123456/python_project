# import requests
# proxy = {"http": "52.149.152.236:80"}
# # proxy = {'HTTP': '36.249.118.60:9999'}
# # url = "https://www.kuaidaili.com"
# i=1
# url = "http://www.kxdaili.com/dailiip/1/{}.html".format(str(i))
# headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#            'Connection': 'close'}
# res = requests.get(url=url, headers=headers, verify=False,
#                    allow_redirects=False, timeout=15, proxies=proxy)
# print(res.text)

# -------------------------2------------------
# content ={'HTTP': '113.195.235.105:9999', 'http': 'http://127.0.0.1:10809', 'https': 'https://127.0.0.1:10809', 'ftp': 'ftp://127.0.0.1:10809'}
# # print(type(content))
# # print(type(content.items()))
# item = list(content.items())[0]
# # print(tmp)
# # ls = list(tmp)[1].split(':')[0]
# # print(ls)
# item = {'{}'.format(item[0]):'{}'.format(item[1])}
# print(item)

# -------------------------3------------------
# import requests
# import re
# url = "http://www.xiladaili.com/gaoni/"
# headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#            'Connection': 'close'}
# # proxy = {"http": "52.149.152.236:80"}
# proxy = {'HTTP': '36.249.118.60:9999'}
# res = requests.get(url=url, headers=headers, verify=False,
#                    allow_redirects=False, timeout=15,proxies=proxy)
# pattern = "<tr>[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>(.*?)</td>"
# items = re.findall(pattern, res.text)
# for item in items:
#     print(item)

# -------------------------4------------------
# import requests
# import pymysql
# import time
# def write_to_mysql1(target):
#     db = pymysql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='myron123',
#         database='crawel'
#     )
#     cursor = db.cursor()
#     sql = 'insert into xiaohuan_dl(target) values("{}")'.format(target)
#     cursor.execute(sql)
#     print('插入成功')
#     db.commit()
#
#
# def write_to_mysql2(target):
#     db = pymysql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='myron123',
#         database='crawel'
#     )
#     cursor = db.cursor()
#     sql = 'insert into xiaohuan_ndl(target) values("{}")'.format(target)
#     cursor.execute(sql)
#     print('插入成功')
#     db.commit()
#
# with open("python爬虫/xiaohuan_dl_http.txt",'r') as f:
#     try:
#         for ip in f.readlines():
#             print(ip)
#             url = "http://icanhazip.com"
#             headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#                        'Connection': 'close'}
#             # proxy = {"HTTP": "52.149.152.236:80"}
#             proxy = {'HTTP': '{}'.format(ip)}
#             res = requests.get(url=url, headers=headers, verify=False,
#                                allow_redirects=False, timeout=15,proxies=proxy)
#             time.sleep(3)
#             item = list(proxy.items())[0]
#             print(res.text)
#             item = {'{}'.format(item[0]): '{}'.format(item[1])}
#             tg = list(item.values())[0].split(':')[0]
#             print(tg)
#             if res.status_code == 200:
#                 # print(item)
#                 write_to_mysql1(item)
#                 if tg in res.text.strip():
#                     print("gn ok")
#                     write_to_mysql2(item)
#     except Exception as e:
#         print(e)

# import requests
# headers = {
#             "User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
#             "referer": "https://ip.ihuan.me/ti.html",
#             'Connection': 'close',
#             "content-type": "application/x-www-form-urlencoded",
#             "upgrade-insecure-requests": "1"
#         }
# url = "https://ip.ihuan.me/tqdl.html"
# data ={
# "num": "3000",
# "port": "",
# "kill_port": "",
# "address":"",
# "kill_address":"",
# "anonymity": "2",
# "type": "0",
# "post": "1",
# "sort": "4",
# "key": "ed9a2751fd1065417ebdd922d7815522",
# }
# data ="num=3000&port=&kill_port=&address=&kill_address=&anonymity=2&type=0&post=1&sort=4&key=4777199f42e757563fb31b0580c81741"
# proxy = {'http': 'http://112.111.77.93:9999'}
# proxy = {'http': 'http://23.101.7.121:80'}
# proxy = {'http': 'http://127.0.0.1:10086'}
# proxy = "http://127.0.0.1:9743"
# headers = {
#     "User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
#     'authority': 'ip.ihuan.me',
#     'upgrade-insecure-requests': '1',
#     'method': 'GET', b
#     'path': '/tqdl.html',
#     'scheme': 'https',
#     'cookie': '__cfduid=d072498ce36e615dea860d269bd9f06081547051697; Hm_lvt_8ccd0ef22095c2eebfe4cd6187dea829=1550409446,1550478213; cf_clearance=5d25f34b61c83053c92f562a03a6468b26879aca-1550498485-1800-220; Hm_lpvt_8ccd0ef22095c2eebfe4cd6187dea829=1550498501',
#     'origin': 'https://ip.ihuan.me',
#     'referer': 'https://ip.ihuan.me/ti.html',
#
# }
# data = {
#     'num': '100',
#     'port': '',
#     'kill_port': '',
#     'anonymity': '2',
#     'type': '',
#     'post': '',
#     'sort': '1',
#     'key': '96c963d523c461a5d6602b7cf1e2c416'
# }


# res = requests.post(url, data=data,headers=headers, verify=False,
#                        allow_redirects=False, timeout=10)
# print(res.text)
# --------------测试高匿ip-------------------
import requests
# proxy = {'http': 'http://220.174.236.211:8091'} #高匿
# proxy = {'http':'http://223.242.224.219:9999'} #连接失败
# proxy = {'http': 'http://121.40.108.76:80'} #高匿
# proxy = {'https': 'https://223.241.116.109:8888'} #透明
# proxy = {'https': 'https://183.166.111.61:9999'} #透明
# proxy = {'http': 'http://188.165.16.230:3129'} #高匿
# proxy = {'http': 'http://5.196.23.219:80'} #高匿
# proxy = {'http': 'http://190.217.39.174:8081'} #高匿
proxy = {'http': 'http://51.158.186.242:8811'} #高匿
url = "http://httpbin.org/get"
# url = "http://icanhazip.com"
# url = "https://ifconfig.me/ip"
# url = "http://www.google.com"
# url = "https://api.myip.com/"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
           'Connection': 'close'}
res = requests.get(url=url, headers=headers, verify=False,
                   allow_redirects=False, timeout=15,proxies=proxy)
# print(proxy)
print(res.text)
# p= list(proxy.values())[0].split(':')[1][2:].split('.')
# p = str(p[1])+"."+str(p[2])+"."+str(p[3])
# print(p)