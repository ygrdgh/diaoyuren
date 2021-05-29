# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 12:05
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : conftest.py
# @Software: PyCharm

import os
import pytest
from appium import webdriver
from pages.page_action import PageAction


driver = None

@pytest.fixture(scope='session')
def handler():

    caps = {"platformName": "Android",
            "platformVersion": "5",
            "deviceName": "127.0.0.1:21503",
            "appPackage": "com.lchr.diaoyu",
            "appActivity": "com.lchr.diaoyu.SplashActivity",
            "noReset": True,
            "newCommandTimeout": 6000,
            "skipServerInstallation": True,
            "automationName": "UiAutomator2",
            "ensureWebviewsHavePages": True}

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    pa = PageAction(driver)
    pa.sleep(8)

    yield driver, pa

    driver.quit()

def pytest_configure(config):
    markers = ['smoke', 'last']
    for mark in markers:
        config.addinivalue_line('markers', mark)