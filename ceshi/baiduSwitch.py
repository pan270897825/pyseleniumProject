# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 3:12
# @Author  : Tomato
# @File    : baiduSwitch.py
# @Software: PyCharm

# coding=utf-8
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.title)
time.sleep(1)

driver.find_element_by_xpath("//*[@id='s-top-left']/a[@class='mnav c-font-normal c-color-t']").click()
print(driver.current_window_handle)  # 输出当前窗口句柄
print(driver.title)
handles = driver.window_handles  # 获取当前全部窗口句柄集合
print(handles)  # 输出句柄集合

for handle in handles:  # 切换窗口
    if handle != driver.current_window_handle:
        print('switch to second window', handle)
        driver.close()  # 关闭第一个窗口
        time.sleep(1)
        driver.switch_to.window(handle)  # 切换到第二个窗口
        print(driver.title)

time.sleep(3)
driver.quit()
