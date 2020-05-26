# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 16:11
# @Author  : Tomato
# @File    : TestRunner.py
# @Software: PyCharm
import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

# suite = unittest.TestSuite()
# suite.addTest(ViewNBANews('test_view_nba_views'))

# suite = unittest.TestSuite(unittest.makeSuite(ViewNBANews))

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLTestRunner.html"
fp = open(HtmlFile, "wb")

# 构建suite

suite = unittest.TestLoader().discover("testsuits")

if __name__ == '__main__':
    # 执行用例
    # runner = unittest.TextTestRunner()

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件

    runner.run(suite)
    fp.close()

