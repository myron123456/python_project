# -*- codeing=utf-8 -*-
# @Time:2021/3/18 9:32
# @Author:
# @File:youdao.py
# @Software:PyCharm
import requests
from fake_useragent import UserAgent
import time
import random
import hashlib
requests.packages.urllib3.disable_warnings()



# 第一步通过先访问主页面拿到cookie，再拿着cookie去访问接口页面
# 注意:response.cookies是CookieJar类型
# 使用requests.utils.dict_from_cookiejar，能够实现把cookiejar对象转化为字典
#
# 第二步加上破解的参数post请求接口
# Math.random();//所得到的的值是0-1之间的 随机数，每次刷新都不同
# parseInt(10 * Math.random(), 10); 生成0-9之间的随机数字
# sign: n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")
# python3下md5加密字符串
# import hashlib
# text= "待加密信息"
# md=hashlib.md5()#创建md5对象
# md.update(text.encode(encoding="utf-8"))
# text_md5=md.hexdigest()#md5加密后
# print(text_md5)

# req= requests.session()
# def get_cookie():
#     url_first = "http://fanyi.youdao.com/"
#     ua_obj = UserAgent()
#     ua = ua_obj.random
#     headers1 = {
#         "user-agent":ua
#     }
#     res = req.get(url_first,headers=headers1,timeout=10,verify=False,allow_redirects=False)
#     cookie = requests.utils.dict_from_cookiejar(res.cookies)
#     print(cookie)
#     return cookie

# def generate_params():

minisecond = int(time.time() * 1000)
# print(minisecond)
cookie_number = minisecond
salt_number = minisecond + random.randint(0,9)
name = input("please input keywords")
sign_str = u"fanyideskweb" + str(name) + str(salt_number) + "Tbh5E8=q6U3EXe+&L[4c@"
md=hashlib.md5()#创建md5对象
md.update(sign_str.encode(encoding="utf-8"))
sign_md5=md.hexdigest()#md5加密后
print(sign_md5)
def get_content():
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    # cookie = get_cookie()
    headers = {
            "cookie":"OUTFOX_SEARCH_USER_ID=-688426475@10.169.0.83; JSESSIONID=aaa5wqg-BiNSw5UwO9cHx; OUTFOX_SEARCH_USER_ID_NCOO=174353744.79874358; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; SESSION_FROM_COOKIE=www.baidu.com; UM_distinctid=1784933c6a142a-09468ea9544922-52183e12-100200-1784933c6a23c4; ___rl__test__cookies=" + str(cookie_number),
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    }
    # headers['cookie'] = cookie
    data = {
        "i": name,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt_number),
        "sign": str(sign_md5),
        "lts": str(minisecond),
        "bv": "59abf8904f967556d4f7669150a903d8",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    res = requests.post(url,headers=headers,data=data,verify=False,timeout=15)
    print(res.content.decode('utf-8'))

get_content()