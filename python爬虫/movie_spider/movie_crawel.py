import os
import re

import requests
import multiprocessing

requests.packages.urllib3.disable_warnings()




def crawel_url(url,proxy,headers):
    res = requests.get(url, headers=headers, timeout=15, verify=False, proxies=proxy)
    result = res.text
    # result_list = result.split("#EXTINF:[\d]+?.[\d]+?,\n")
    pattern = "#EXTINF:[\d]+.[\d]+,\n(.*)"
    result_list = re.findall(pattern, result)
    # print(result_list)
    print(len(result_list))
    return result_list

def crawel_content(target_url,proxy,headers):
    target_url =str(target_url).replace("https","http")
    res = requests.get(target_url, headers=headers, timeout=15, verify=False, proxies=proxy)
    # result = res.content
    return res

def save_ts(filename,content):
    # filename = re.findall("/hls/(.*?).ts",target_url)[0]
    # print(filename)
    with open("./myzw_movie/{}.ts".format(filename),'wb') as fp:
        fp.write(content)


def main():
    url = "http://v3.dious.cc/20210101/zytW3Egy/1000kb/hls/index.m3u8"
    proxy = {"http": "http://39.106.223.134:80"}
    # proxy = {'http': 'http://218.60.8.99:3129'}
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "v3.dious.cc",
        "Origin": "https://jx.618g.com",
        "Referer": "https://jx.618g.com/",
        "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    }
    result_list = crawel_url(url,proxy,headers)
    # os.makedirs("./myzw_movie", exist_ok=True)
    # for target_url in result_list:
    #     content = crawel_content(target_url,proxy,headers)
    #     # print(content)
    for i in range(1414,len(result_list)+1):
        target_url = result_list[i-1]
        res = crawel_content(target_url, proxy, headers)
        if res.status_code == 200:
            content = res.content
            save_ts(i,content)
            # filename = re.findall("/hls/(.*?).ts",target_url)[0]
            jindu = i / len(result_list) * 100
            print("\r进度:"+str(jindu)[:4] + "%", end="")

        else:
            filename = re.findall("/hls/(.*?).ts",target_url)[0]
            print(filename,"访问失败,重新处理")
            # i = i-1
            result_list.insert(i,result_list[i])

    print("保存完毕")
main()