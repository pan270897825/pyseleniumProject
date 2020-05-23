# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 2:58
# @Author  : Tomato
# @File    : viewNBANews.py
# @Software: PyCharm
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.baidusearchPage import BaidusearchPage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接
        search = BaidusearchPage(self.driver)
        # baiduhome.click_news()
        # self.driver.find_element_by_xpath("//*[@id='u1']/a[@name='tj_trnews']").click()
        search.click_news()
        new_title = search.get_page_title()

        print(new_title)


if __name__ == '__main__':
    unittest.main()
