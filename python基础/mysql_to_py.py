import pymysql
import pandas as pd
# def read_proxys():
#     db = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="myron123",
#         database="crawel",
#     )
#     cursor = db.cursor()
#     sql = "select distinct target from proxy;"
#     cursor.execute(sql)
#     proxys = cursor.fetchall()
#     db.commit()
#     return proxys

def proxy_list():
    proxys = read_proxys()
    proxy_list = []
    for i in range(0,len(proxys)-1):
        proxy = proxys[i][0]
        proxy_list.append(proxy)
        # print(proxy_list)
    return proxy_list

# def write_to_proxy_txt():
#     proxys = read_proxys()
#     for i in range(0,len(proxys)-1):
#         proxy = proxys[i][0]
#         with open('proxys.txt','a') as f:
#             f.write(proxy+"\n")
# write_to_proxy_txt()


