# -*- codeing=utf-8 -*-
# @Time:2021/3/17 14:14
# @Author:
# @File:test_tuozhuai.py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver import ActionChains

url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser = webdriver.Chrome()
browser.get(url)
browser.switch_to_frame("iframeResult")
actions = ActionChains(browser)
position1 = browser.find_element_by_id("draggable")
position2 = browser.find_element_by_id("droppable")
actions.drag_and_drop(position1, position2)
actions.perform()
# browser.close()
