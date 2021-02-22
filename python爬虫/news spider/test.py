import requests
from fake_useragent import UserAgent
import time
from lxml import etree
import json
import base64
requests.packages.urllib3.disable_warnings()


def crawel_kuaixun(url):
    user_agent = UserAgent()
    ua = user_agent.random
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
        # "Host": "gateway.36kr.com",
        'content-type':'application/json',
        # "Origin":"https://www.36kr.com",
        # "sec-ch-ua":'"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        # "sec-ch-ua-mobile": "?0",
        # "Accept": "*/*",
        # "Sec-Fetch-Site": "same-site",
        # "Sec-Fetch-Mode": "cors",
        # "Sec-Fetch-Dest": "empty",
        # "Referer": "https://www.36kr.com/",
        # "Accept-Encoding": "gzip,deflate",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Connection": "close",
        # "Cookie": 'device-uid=14494720-5422-11eb-9c04-6948f8f5cb42; download_animation=1; Hm_lvt_1684191ccae0314c6254306a8333d090=1613889202; Hm_lvt_713123c60a0e86982326bae1a51083e1=1613889202; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22176f21160a7393-0e4256e2993ca-c791039-1327104-176f21160a82fd%22%2C%22%24device_id%22%3A%22176f21160a7393-0e4256e2993ca-c791039-1327104-176f21160a82fd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; acw_tc=2760829a16138975250686995ead9989af64b40fe2b4847a0bc5d591448959; Hm_lpvt_1684191ccae0314c6254306a8333d090=1613897606; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1613897606;',
    }
    proxy ={"http": "http://5.39.17.96:80"}
    # time1 = time.time()
    # time1 = str(time1).replace(".","")[:13]
    # print(time1)
    # time.sleep(0.1)
    # time2 = time.time()
    # time2 = str(time2).replace(".", "")[:13]
    # print(time2)
    # post_data = "{\"firstId\":1105265542744840,\"lastId\":1105046704016130,\"firstCreateTime\":1613898894754,\"lastCreateTime\":1613885503322}"
    # print(post_data)
    # post_data = base64.b64encode(post_data.encode("utf-8")).decode("utf-8")
    # print(post_data)
    post_data = "eyJmaXJzdElkIjoxMTA3OTk5MDQzNjYwMDM1LCJsYXN0SWQiOjExMDc3Nzk2Mzg0Mzc4OTUsImZpcnN0Q3JlYXRlVGltZSI6MTYxMzg5ODg5NDc1NCwibGFzdENyZWF0ZVRpbWUiOjE2MTM4ODU1MDMzMjJ9"
    data = '{"partner_id":"web","timestamp":1613897745666,"param":{"pageSize":20,"pageEvent":1,"pageCallback":"'+post_data+'","siteId":1,"platformId":2}}'
    res = requests.post(url=url, headers=headers, data=data,verify=False,proxies=proxy,timeout=15)
    # print(res.text)
    return res.text
url = "https://gateway.36kr.com/api/mis/nav/newsflash/flow"
print(crawel_kuaixun(url))
1613901678854

