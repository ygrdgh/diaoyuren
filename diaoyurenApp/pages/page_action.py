# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 11:49
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : page_action.py
# @Software: PyCharm

from common.bases.base_page import BasePage
from locators.login_locator import LoginLocator
from test_data.data_for_login import success_data
from locators.main_page_locator import MainPageLocator
from locators.mine_page_locator import MinePageLocator
from locators.setting_page_locator import SettingPage
from run import logger


class PageAction(BasePage):
    def login(self, username, password):
        self.send_data(LoginLocator.username_input_loc, username)
        self.send_data(LoginLocator.password_input_loc, password)
        self.click_element(LoginLocator.login_btn_loc)

    def go_to_me_page(self):
        self.click_element(MainPageLocator.me_icon_loc)
        self.sleep(3)

    def is_use_login(self):
        try:
            if self.search_element(MinePageLocator.click_login_text_loc):
                return False
        except Exception as e:
            logger.info('未找到页面登录元素:{}'.format(MinePageLocator.click_login_text_loc))
            logger.error(e)
            return True

    def logout(self):
        try:
            self.click_element(MinePageLocator.setting_btn_loc)
            self.sleep(2)
            self.click_element(SettingPage.logout_btn_loc)
            self.sleep(2)
            self.click_element(SettingPage.logout_confirm_loc)
            self.sleep(3)
            logger.info('退出登录成功')
        except Exception as e:
            logger.warning('退出登陆失败')
            logger.error(e)

    def go_to_login_page(self):
        try:
            self.go_to_me_page()
            if self.is_use_login():
                self.logout()
            else:
                self.click_element(MinePageLocator.click_login_text_loc)
                self.sleep(2)
                self.click_element(LoginLocator.fishman_account_text_loc)
                self.sleep(2)
        except Exception as e:
            logger.info('进入快捷登录')
            logger.error(e)

    def is_nickname_exists(self):
        try:
            if self.search_element(MinePageLocator.nickname_loc):
                return True
        except Exception as e:
            logger.warning('未发现昵称：{}'.format(MinePageLocator.nickname_loc))
            logger.warning(e)
            return False
