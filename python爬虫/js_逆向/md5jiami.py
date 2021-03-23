# -*- codeing=utf-8 -*-
# @Time:2021/3/19 16:47
# @Author:
# @File:md5jiami.py
# @Software:PyCharm
import hashlib
text= "待加密信息"
md=hashlib.md5()#创建md5对象
md.update(text.encode(encoding="utf-8"))
text_md5=md.hexdigest()#md5加密后
print(text_md5)