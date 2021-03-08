# -*- codeing=utf-8 -*-
# @Time:2021/3/5 10:44
# @Author:
# @File:jpg_yzm.py
# @Software:PyCharm
import pytesseract
from PIL import Image

# image = Image.open('F:/pythonProject/python爬虫/yzm/jpg/{}.jpg'.format(i))
# image=image.convert('L')
# threshold=150
# table=[]
# for i in range(256):
#     if i <threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image=image.point(table,'1')
# result = pytesseract.image_to_string(image)
maxpage=1000
result_list = []
for i in range(1,maxpage+1):
    image = Image.open('F:/pythonProject/python爬虫/yzm/jpg/{}.jpg'.format(i))
    # with open("./jpg/{}.jpg".format(i),"r") as f:
    #     content = f.readlines()
    result = pytesseract.image_to_string(image).split("\x0c")[0].strip()
    if result != "":
        # with open("./jpg1/{}.jpg".format(result), "wb") as fp:
        #     fp.write(content)
        print("\r"+result,end="")
        print("\t\t"+str(i),end="")
        result_list.append(result)
        print("\t\t识别率:"+str((i-len(result_list))/i*100)[:5]+"%",end="")
        print("\t\t进度:" + str((i /(maxpage + 1) * 100))[:5] + "%", end="")
print(result)
