# -*- codeing=utf-8 -*-
# @Time:2021/3/18 9:32
# @Author:
# @File:youdao.py
# @Software:PyCharm

import chardet

# import requests
# url = "http://www.baidu.com"
# res = requests.get(url)
# print(res.text)
# # print(chardet.universaldetector(res.text))
# print(res.encoding)

strs = "aadfjkl;"
strs.encode("utf-8")
print(type(strs))
strs.encode("gbk")
print(strs)
