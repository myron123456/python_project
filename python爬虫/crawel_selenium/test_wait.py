# -*- codeing=utf-8 -*-
# @Time:2021/3/17 17:48
# @Author:
# @File:test_wait.py
# @Software:PyCharm
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://spa2.scrape.center/page/2")
# input = browser.find_element_by_class_name("Tabs-link")
# browser.implicitly_wait(30)
print(browser.page_source)
browser.close()
