# -*- codeing=utf-8 -*-
# @Time:2021/3/17 16:12
# @Author:
# @File:test_getattribute.py
# @Software:PyCharm
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")
logo = browser.find_element_by_class_name("Tabs-link")
print(logo)
# print(logo.get_attribute("href"))
print(logo.text, logo.id, logo.size, logo.location, logo.tag_name)
