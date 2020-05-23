# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 1:08
# @Author  : Tomato
# @File    : baidusearchPage.py
# @Software: PyCharm
from framework.basepage import BasePage


class BaidusearchPage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    # news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"
    news_link = "xpath=>//*[@id='s-top-left']/a[@class='mnav c-font-normal c-color-t']"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def get_title(self):
        self.sleep(1)
        return self.get_page_title

    def click_news(self):
        self.click(self.news_link)
        self.sleep(2)
