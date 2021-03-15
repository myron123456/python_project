import os
import re
import time
import random
import requests
import multiprocessing
from fake_useragent import UserAgent
requests.packages.urllib3.disable_warnings()
ua =   UserAgent()
ua = ua.random
headers = {
    "Host": "so.gushiwen.cn",
    "Connection": "close",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": 'Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99',
    "sec-ch-ua-mobile": "?0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "ASP.NET_SessionId=j21elx4mkaaatl4y0zr01exz; Hm_lvt_9007fab6814e892d3020a64454da5a55=1615032449,1615035886; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1615035886; codeyzgswso=fa1559135934c4cb"
    # "Cookie":"ASP.NET_SessionId=j21elx4mkaaatl4y0zr01exz; Hm_lvt_9007fab6814e892d3020a64454da5a55=1615032449,1615035886; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1615035886; codeyzgswso=6978932db633228c"
     }
url = "https://so.gushiwen.cn/RandCode.ashx"

os.makedirs("jpg", exist_ok=True)
maxpage = 18000
print("开始下载图片...")

for i in range(15001,maxpage+1):
    try:
        # proxy_list = [{'http': 'http://112.245.17.202:8080'}, {'http': 'http://5.196.23.219:80'}, {'http': 'http://51.158.186.242:8811'}, {'http': 'http://39.106.223.134:80'}, {'http': 'http://220.174.236.211:8091'}, {'http': 'http://34.203.142.175:80'}, {'http': 'http://192.109.165.129:80'}, {'http': 'http://191.101.39.81:80'}, {'http': 'http://88.99.10.254:1080'}, {'http': 'http://88.99.10.251:1080'}, {'http': 'http://220.174.236.211:8091'}, {'http': 'http://218.59.139.238:80'}, {'http': 'http://39.106.223.134:80'}, {'http': 'http://47.106.162.218:80'}, {'http': 'http://78.47.16.54:80'}, {'http': 'http://5.196.23.219:80'}, {'http': 'http://88.99.10.251:1080'}, {'http': 'http://51.158.107.202:9999'}, {'http': 'http://88.99.10.254:1080'}, {'http': 'http://191.101.39.81:80'}, {'http': 'http://191.101.39.238:80'}, {'http': 'http://148.251.153.6:1080'}, {'http': 'http://186.226.174.193:8080'}, {'http': 'http://78.47.16.54:80'}, {'http': 'http://39.100.18.200:8080'}, {'http': 'http://198.50.163.192:3129'}, {'http': 'http://195.53.49.11:3128'}, {'http': 'http://148.251.153.6:1080'}, {'http': 'http://51.75.147.44:3128'}, {'http': 'http://178.128.83.219:8899'}, {'http': 'http://191.101.39.238:80'}, {'http': 'http://142.4.203.248:3128'}, {'http': 'http://46.35.249.189:41419'}, {'http': 'http://221.141.130.183:33741'}, {'http': 'http://185.38.111.1:8080'}]
        proxy_list = [{'http': 'http://43.248.24.157:51166'}, {'http': 'http://218.59.139.238:80'}, {'http': 'http://5.196.23.219:80'}, {'http': 'http://51.158.186.242:8811'}, {'http': 'http://39.106.223.134:80'}, {'http': 'http://191.101.39.27:80'}, {'http': 'http://122.226.57.70:8888'}, {'http': 'http://220.174.236.211:8091'}, {'http': 'http://47.75.90.57:80'}, {'http': 'http://74.143.245.221:80'}, {'http': 'http://34.203.142.175:80'}, {'http': 'http://191.101.39.154:80'}, {'http': 'http://106.14.198.6:8080'}, {'http': 'http://192.109.165.129:80'}, {'http': 'http://191.101.39.81:80'}, {'http': 'http://88.99.10.254:1080'}, {'http': 'http://88.99.10.251:1080'}, {'http': 'http://220.174.236.211:8091'}, {'http': 'http://218.59.139.238:80'}, {'http': 'http://39.106.223.134:80'}, {'http': 'http://47.106.162.218:80'}, {'http': 'http://78.47.16.54:80'}, {'http': 'http://115.75.1.184:8118'}, {'http': 'http://88.99.10.251:1080'}, {'http': 'http://88.99.10.254:1080'}, {'http': 'http://186.226.174.193:80'}, {'http': 'http://191.101.39.81:80'}, {'http': 'http://191.101.39.238:80'}, {'http': 'http://148.251.153.6:1080'}, {'http': 'http://180.94.69.66:8080'}, {'http': 'http://118.24.89.206:1080'}, {'http': 'http://39.100.18.200:8080'}, {'http': 'http://106.14.198.6:8080'}, {'http': 'http://78.47.16.54:80'}, {'http': 'http://5.39.17.96:80'}, {'http': 'http://51.158.172.165:8811'}, {'http': 'http://51.158.107.202:9999'}, {'http': 'http://191.101.39.238:80'}, {'http': 'http://148.251.153.6:1080'}, {'http': 'http://118.24.88.66:1080'}, {'http': 'http://118.24.172.149:1080'}, {'http': 'http://67.225.164.154:80'}, {'http': 'http://144.217.101.245:3129'}, {'http': 'http://128.14.178.94:3128'}, {'http': 'http://195.53.49.11:3128'}, {'http': 'http://152.67.24.187:80'}, {'http': 'http://103.28.121.58:3128'}, {'http': 'http://202.109.157.63:9000'}, {'http': 'http://150.109.32.166:80'}, {'http': 'http://136.232.209.70:47423'}, {'http': 'http://180.94.69.66:8080'}, {'http': 'http://86.34.197.6:23500'}, {'http': 'http://142.4.203.248:3128'}, {'http': 'http://221.141.130.183:33741'}, {'http': 'http://185.38.111.1:8080'}, {'http': 'http://193.105.107.156:8080'}, {'http': 'http://103.152.5.80:8080'}, {'http': 'http://202.152.51.44:8080'}, {'http': 'http://118.24.89.122:1080'}, {'http': 'http://161.35.4.201:80'}, {'http': 'http://159.203.44.177:3128'}, {'http': 'http://193.233.9.167:57625'}, {'http': 'http://176.9.85.13:3128'}, {'http': 'http://83.41.4.229:8080'}, {'http': 'http://81.95.226.138:3128'}, {'http': 'http://77.232.100.132:80'}, {'http': 'http://122.224.65.197:3128'}, {'http': 'http://51.75.144.32:3128'}, {'http': 'http://18.139.108.183:3128'}, {'http': 'http://212.98.243.155:3128'}, {'http': 'http://49.75.59.242:3128'}, {'http': 'http://118.24.128.46:1080'}, {'http': 'http://62.171.144.29:3128'}, {'http': 'http://37.235.97.14:3128'}, {'http': 'http://3.36.65.133:80'}, {'http': 'http://218.60.8.99:3129'}, {'http': 'http://209.127.55.18:3128'}, {'http': 'http://37.235.96.200:3128'}, {'http': 'http://104.238.81.186:56220'}, {'http': 'http://178.205.169.210:3128'}, {'http': 'http://212.102.52.6:3128'}, {'http': 'http://60.199.134.97:3128'}, {'http': 'http://140.238.39.99:8080'}, {'http': 'http://51.79.79.111:3128'}]
        proxy = {'http': 'http://27.158.30.240:26156'}
        proxy = {'http': 'http://59.63.61.235:34957'}
        proxy = proxy_list[random.randint(0,len(proxy_list)-1)]
        # res1 = requests.get("http://httpbin.org/ip",proxies = proxy,timeout=15)
        # print(res1.text)
        res = requests.get(url=url,proxies=proxy,headers=headers, timeout=15, verify=False, allow_redirects=False)
        # print(res.content)
        # time.sleep(random.randrange(3,6))
        result = res.content
        if res.status_code==200:
            with open("./jpg/{}.jpg".format(i),"wb") as fp:
                fp.write(result)
            print("\r进度:"+str((i/(maxpage))*100)[:5]+"%",end="")
        else:
            i = i-1
            print("下载错误")
    except Exception as e:
        print(e)
print("下载完成")