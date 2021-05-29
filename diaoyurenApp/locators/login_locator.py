# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 11:41
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : login_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class LoginLocator:

    fishman_account_text_loc = (By.ID, 'com.lchr.diaoyu:id/tv_account_login')
    username_input_loc = (By.ID, 'com.lchr.diaoyu:id/user_id')
    password_input_loc = (By.ID, 'com.lchr.diaoyu:id/passwd_id')
    login_btn_loc = (By.ID, 'com.lchr.diaoyu:id/btn_login')