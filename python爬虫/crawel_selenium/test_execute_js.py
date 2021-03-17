# -*- codeing=utf-8 -*-
# @Time:2021/3/17 15:45
# @Author:
# @File:test_execute_js.py
# @Software:PyCharm
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
browser.execute_script('alert("To Bottom")')
