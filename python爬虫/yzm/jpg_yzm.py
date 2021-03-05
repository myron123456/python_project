# -*- codeing=utf-8 -*-
# @Time:2021/3/5 10:44
# @Author:
# @File:jpg_yzm.py
# @Software:PyCharm
import pytesseract
from PIL import Image

image = Image.open('C://Users/Administrator/Desktop/爬虫/yzm/CheckCode.jpg')
print(pytesseract.image_to_string(image))
