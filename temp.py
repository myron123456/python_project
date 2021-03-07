import requests
from fake_useragent import UserAgent
import random
import time
requests.packages.urllib3.disable_warnings()

ua = UserAgent()
ua = ua.random
headers = {
    "User-Agent": ua,

}
# url = "https://so.csdn.net/api/v2/search?q=python+%E7%88%AC%E8%99%AB&t=userinfo&p=1&s=0&tm=0&lv=-1&ft=0&l=&u=&platform=pc"
# url = "http://113.31.118.145:8206"
url = "http://httpbin.org/get"
# proxy ={'http': 'http://89.187.177.107:80'}
# proxy = {'http': 'http://8.210.153.2:80'}
# proxy = {'http': 'http://218.60.8.99:3129'} #特殊，返回两个
# proxy = {'http': 'http://60.205.132.71:80'} #特殊
# proxy = {'http': 'http://15.237.10.173:8080'} #特殊
# proxy = {'http': 'http://39.98.39.55:80'}
# url = "https://mp.weixin.qq.com/s/vB4vgXbHjyqcObcQYkdrXg"
# proxy_list = [{'http': 'http://112.245.17.202:8080'}, {'http': 'http://5.196.23.219:80'}, {'http': 'http://51.158.186.242:8811'}, {'http': 'http://39.106.223.134:80'}, {'http': 'http://220.174.236.211:8091'}, {'http': 'http://34.203.142.175:80'}, {'http': 'http://192.109.165.129:80'}, {'http': 'http://191.101.39.81:80'}, {'http': 'http://88.99.10.254:1080'}, {'http': 'http://88.99.10.251:1080'}, {'http': 'http://220.174.236.211:8091'}, {'http': 'http://218.59.139.238:80'}, {'http': 'http://39.106.223.134:80'}, {'http': 'http://47.106.162.218:80'}, {'http': 'http://78.47.16.54:80'}, {'http': 'http://5.196.23.219:80'}, {'http': 'http://88.99.10.251:1080'}, {'http': 'http://51.158.107.202:9999'}, {'http': 'http://88.99.10.254:1080'}, {'http': 'http://191.101.39.81:80'}, {'http': 'http://191.101.39.238:80'}, {'http': 'http://148.251.153.6:1080'}, {'http': 'http://186.226.174.193:8080'}, {'http': 'http://78.47.16.54:80'}, {'http': 'http://39.100.18.200:8080'}, {'http': 'http://198.50.163.192:3129'}, {'http': 'http://195.53.49.11:3128'}, {'http': 'http://148.251.153.6:1080'}, {'http': 'http://51.75.147.44:3128'}, {'http': 'http://178.128.83.219:8899'}, {'http': 'http://191.101.39.238:80'}, {'http': 'http://142.4.203.248:3128'}, {'http': 'http://46.35.249.189:41419'}, {'http': 'http://221.141.130.183:33741'}, {'http': 'http://185.38.111.1:8080'}]
# proxy = {'http': 'http://27.158.30.240:26156'}
# proxy = {'http': 'http://123.52.179.233:40240'}
# proxy = proxy_list[random.randint(0,len(proxy_list)-1)]
proxy = {'http': 'http://183.89.144.131:8080'}
# for i in range(1,6):
#     res = requests.get(url=url, headers=headers, verify=False,
#                        timeout=15, allow_redirects=False,proxies=proxy)
#     time.sleep(random.randrange(5,18))
res = requests.get(url=url, headers=headers, verify=False,
                       timeout=15, allow_redirects=False,proxies=proxy)
print(res.text,res.status_code)
