# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 3:15
# @Author  : Tomato
# @File    : basepage.py.py
# @Software: PyCharm
import os.path
import time

from selenium.common.exceptions import NoSuchElementException

from framework.logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # print(selector_by)
        # print(selector_value)

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 或者网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    """
    ------------------------------------------------------------------------------------------------------
    添加方法
    """

    # 刷新当前页面
    def refresh(self):
        try:
            self.driver.back()
            logger.info("Click forward on refresh successful")
        except Exception as e:
            logger.error(" refresh failed Exception found %s" % e)

    # 当前页面的标题显示的字段
    def current_url(self):
        title = self.driver.title
        logger.info("Get the URL of the title page." % title)
        return title

        # 获取当前本文重

    def text_mes(self, selector):
        text_mes = self.find_element(selector).text
        logger.info("Get the text of the element page." % text_mes)
        return text_mes

    def iframe(self, selector):
        el = self.find_element(selector)
        try:
            self.driver.switch_to.frame(el)
            # 操作目标元素，这个目标元素在 iframe1里面，这里就是百度文本输入框输入文字
            self.driver.switch_to.default_content()
            logger.info("Click forward on Iframe switching successful")
        except Exception as e:
            logger.error("Iframe switching failed  Exception found %s" % e)

        # 处理Alert弹窗

    def Handle_alert(self, value):
        try:
            self.sleep(2)
            if value == 1:
                self.driver.switch_to_alert().accept()
                # 点击弹出里面的确定按钮
                logger.info("Handle alert pop ups is accept %s")
            elif value == 2:
                self.driver.switch_to_alert().dismiss()
                logger.info("Handle alert pop ups is dismiss %s")
                # 点击弹出上面的X按钮
            else:
                logger.info("Handle alert pop ups is failed %s" % value)
        except Exception as e:
            logger.error("Handle alert failed  Exception found %s" % e)

    def switch_window(self):
        handles = self.driver.window_handles
        for handle in handles:  # 切换窗口
            if handle != self.driver.current_window_handle:
                self.get_page_title()
                self.driver.close()  # 关闭第一个窗口
                self.driver.switch_to.window(handle)  # 切换到第二个窗口
                logger.info('Close the first window,switch to second window')
                # self.get_page_title()
