# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 2:58
# @Author  : Tomato
# @File    : test_viewNBANews.py
# @Software: PyCharm
import sys
import unittest

from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.baidusearchPage import BaidusearchPage

logger = Logger(logger="ViewNBANews").getlog()


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        # self.driver.close()
        self.driver.quit()

    def test_view_nba_views(self):
        logger.info(sys._getframe().f_code.co_name)
        # 初始化百度首页，并点击新闻链接
        search = BaidusearchPage(self.driver)
        # baiduhome.click_news()
        # self.driver.find_element_by_xpath("//*[@id='u1']/a[@name='tj_trnews']").click()
        search.click_news()
        search.switch_newsWindow()
        new_title = search.get_page_title()
        try:
            assert '百度新闻——海量中文资讯平台' in new_title
            logger.info("Test Pass.")
        except Exception as e:
            logger.error("Test Fail %s" % e)


# if __name__ == '__main__':
    # # 构造测试套件
    # testsuit = unittest.TestSuite()
    #
    # testsuit.addTest(ViewNBANews("test_baidu_ide"))
    #
    # # 设置报告文件保存路径
    # # report_path = os.path.dirname(os.path.abspath('.')) + '/report/'
    # report_path = os.path.dirname(os.getcwd()) + '/report/'
    # print("--------------------------------------------------------------")
    # print(report_path)
    # # 获取系统当前时间
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #
    # # 设置报告名称格式
    # HtmlFile = report_path + now + 'HTMLTestRunner.html'
    # print(HtmlFile)
    # fp = open(HtmlFile, 'wb')
    #
    # # 初始化一个HTMLTestRunner实例对象，用来生成报告
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"ViewNBANews测试报告", description=u"用例测试情况")
    # # 开始执行测试套件
    #
    # runner.run(testsuit)
    # # 关闭测试报告
    # fp.close()
    # # unittest.main()
    # print(HtmlFile)
