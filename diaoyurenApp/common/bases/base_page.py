# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 11:52
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : base_page.py
# @Software: PyCharm


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from selenium import webdriver
from run import img_dir_path
import time
from run import logger
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def sleep(self, s):
        time.sleep(s)

    def search_element(self, locator):
        logger.info('开始查找页面元素：{}'.format(locator))
        return self.driver.find_element(*locator)


    def click_element(self, locator):
        logger.info('开始点击页面元素：{}'.format(locator))
        self.search_element(locator).click()

    def send_data(self, locator, data):
        logger.info('开始向页面元素发送数据：{}，{}'.format(locator, data))
        self.search_element(locator).send_keys(data)

    def wait_element_visible(self, locator, msg=''):
        try:
            now = datetime.now()
            WebDriverWait(self.driver, 20).\
                until(EC.visibility_of_element_located(locator))
            end = datetime.now()
            cost_time = (end-now).total_seconds()
            logger.info('等待元素可见耗时{}'.format(cost_time))
        except Exception as e:
            logger.info(e)

    def get_element_text(self, locator, msg=""):
        self.wait_element_visible(locator, msg)
        return self.search_element(locator).text


    def save_picture(self, msg=''):
        img_path = img_dir_path + '{0}-{1}.png'.format(msg, time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime()))
        try:
            self.driver.save_screenshot(img_path)
            logger.info('截图成功，图片保存路径为：{}'.format(img_path))
        except Exception as e:
            logger.info('截图失败')
            logger.info(e)

    def is_toast_show(self, msg, timeout=20, poll_frequency=0.5):
        locator = (By.XPATH, '//*[contains(@text,%s)]' %msg)
        try:
            # 等待元素存在方法presence_of_element_located(locator)，使用toast时调用
            WebDriverWait(self.driver, timeout, poll_frequency).\
                until(EC.presence_of_element_located(locator))
            logger.info('找到toast：{}'.format(locator))
            self.save_picture('toast截图')
            return True
        except Exception as e:
            logger.error(e)
            logger.warning('查找toast：{}'.format(locator))
            self.save_picture('未发现toast')
            return False