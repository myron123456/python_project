# -*- codeing=utf-8 -*-
# @Time:2021/3/5 17:48
# @Author:
# @File:quake.py.py
# @Software:PyCharm
# -*- coding: utf-8 -*-
import requests
import json
import random
import time
from fake_useragent import UserAgent

requests.packages.urllib3.disable_warnings()


def crawel_quake_360(url, size, page):
    headers = {
        "Host": "quake.360.cn",
        "Connection": "close",
        "Content-Length": "88",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "233",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "https://quake.360.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://quake.360.cn/quake/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
        "Cookie": "__guid=24002531.990683007926979968.1603762366001.3059; __DC_gid=59612149.875882069.1605753531069.1605753788043.7; Q=u=hfdnq123&n=&le=qKAkMT1vqJE1WGDjoJScoP5lqD==&m=&qid=3273397217&im=1_t0105d6cf9b508f72c8&src=pcw_quake&t=1; Qs_lvt_356657=1608020073; Qs_pv_356657=1384654746430828500; Qs_lvt_344458=1608020094,1608089249; Qs_pv_344458=3832689226728545000,3826139034385491500; __huid=11RNmSFvaABvd4fmFNqTKQqdsfl6xsaBeRRPjt2yKcJDA=; Q_UDID=3036f057-007f-3167-e82d-3de4db16b873; __gid=133660893.820737315.1611798444630.1611798551714.2; cert_common=87405afd-5cf9-496e-8010-b3b5141a8304; T=s=e1f646af21b45a41f932516d97a828a6&t=1614653083&lm=&lf=4&sk=31da1bf568f9db6d6f3c6d2402f81ae5&mt=1614653083&rc=&v=2.0&a=1; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Qs_lvt_357693=1612661372,1614333906,1614653101,1614758260,1614840686; Qs_pv_357693=1187760648818816000,2018287171768366300,2842978706771111000,3119296855707226000,2447604725870278700",

    }
    # proxy = {'http': 'http://112.169.9.162:80'}
    #  proxy = {'http': 'http://175.149.84.238:35522'}
    proxy = {'https': 'https://115.221.126.137:34295'}
    data = '{"size": ' + str(size) + ', "page": ' + str(page) + \
           ', "vul_has_poc": "1","time_start": "2018-01-01", "time_end": "2021-03-04"}'
    # print(data)
    res = requests.post(url, data=data, headers=headers,
                        timeout=15, verify=False)
    print(res.text)
    # with open('tmps.txt', 'w') as f:
    #     f.write(res.text)
    # print('访问成功')
    return res.text


def parse_quake_data(json_data):
    quake_db_list = []
    for i in range(0, 10):
        quake_dict = {}
        quake_dict["vul_cve_id"] = json_data['data'][i]['vul_cve_id']
        quake_dict["vul_detail"] = json_data['data'][i]['vul_detail']
        quake_dict["vul_name"] = json_data['data'][i]['vul_name']
        quake_dict["vul_type"] = json_data['data'][i]['vul_type']
        # print(quake_dict)
        quake_db_list.append(quake_dict)
    return quake_db_list


def main():
    url = "https://quake.360.cn/api/control/vulnerability/db/search/"
    max_page = 611
    size = 10
    for page in range(601, max_page + 1):
        try:
            time.sleep(random.randrange(5, 15))
            html = crawel_quake_360(url, size, page)
            json_data = json.loads(html)
            quake_db_list = parse_quake_data(json_data)
            print(len(quake_db_list) * page)
            for item in quake_db_list:
                with open("quake_data.txt", "a") as f:
                    f.write(json.dumps(item) + '\n')
        except Exception as e:
            print(e)


main()
