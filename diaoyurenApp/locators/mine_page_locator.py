# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 20:41
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : mine_page_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class MinePageLocator:

    nickname_loc = (By.ID, 'com.lchr.diaoyu:id/user_nick_name')
    setting_btn_loc = (By.ID, 'com.lchr.diaoyu:id/iv_top_navi_setting')
    click_login_text_loc = (By.ID, 'com.lchr.diaoyu:id/tv_click2login')
