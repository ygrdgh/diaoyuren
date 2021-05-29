# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 20:41
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : setting_page_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class SettingPage:
    logout_btn_loc = (By.ID, 'com.lchr.diaoyu:id/rtv_setting_logout')
    logout_confirm_loc = (By.ID, 'android:id/button1')
