# -*- codeing=utf-8 -*-
# @Time:2021/3/17 10:32
# @Author:
# @File:test_baidu.py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
try:
    browser.get("http://www.baidu.com")
    input = browser.find_element_by_id("kw")
    input.send_keys("python")
    input.clear()
    input.send_keys("java")
    # input.send_keys(Keys.ENTER)
    button = browser.find_element_by_id("su")
    button.click()
    wait = WebDriverWait(browser, 10)
    time.sleep(15)
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
