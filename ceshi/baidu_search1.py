# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 2:42
# @Author  : Tomato
# @File    : baidu_search.py
# @Software: PyCharm
import sys
import time
import unittest

from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.baidusearchPage import BaidusearchPage

logger = Logger(logger="BaiduSearch1").getlog()


class BaiduSearch1(unittest.TestCase):

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()
        self.driver.close()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        logger.info(sys._getframe().f_code.co_name)

        # self.driver.find_element_by_id('kw').send_keys('selenium')
        # time.sleep(1)
        search = BaidusearchPage(self.driver)
        search.type_search('selenium')
        search.send_submit_btn()
        try:
            assert 'selenium' in search.get_page_title()
            logger.info("Test Pass.")
        except Exception as e:
            logger.error("Test Fail %s" % e)

    def test_search2(self):
        search = BaidusearchPage(self.driver)
        search.type_search('python')  # 调用页面对象中的方法
        search.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        search.get_windows_img()  # 调用基类截图方法


if __name__ == '__main__':
    unittest.main()
