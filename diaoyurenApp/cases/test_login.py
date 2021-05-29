# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 11:50
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : test_login.py
# @Software: PyCharm


from cases.conftest import handler
from pages.page_action import PageAction
from test_data.data_for_login import success_data
from run import logger
from test_data.data_for_login import failed_data
import pytest
import time
import allure

@pytest.fixture(scope='module')
def prepare_to_login(handler):
    handler[1].go_to_login_page()


@allure.epic('钓鱼人APP自动化测试')
@allure.feature('钓鱼人APP自动化测试-登陆功能测试')
@pytest.mark.usefixtures('prepare_to_login')
class TestLogin:

    @allure.story('钓鱼人APP自动化测试正向用例测试')
    @allure.title('登录测试正向用例')
    @pytest.mark.last
    def test_login_success(self, handler):

        logger.info('++++++++++++++开始执行正向用例+++++++++++')
        handler[1].login(success_data['username'], success_data['password'])
        logger.info("登录操作完成")
        time.sleep(3)
        assert handler[1].is_nickname_exists()
        logger.info('+++++++++正向用例测试通过++++++++++')
        handler[1].save_picture('正向用例测试截图')

    @allure.story('钓鱼人APP自动化测试反向用例测试')
    @allure.title('登录测试反向用例')
    @pytest.mark.parametrize('data', failed_data)
    def test_login_failed(self, handler, data):
        logger.info('开始执行反向测试用例：{}'.format(data['name']))
        handler[1].login(data['username'], data['password'])
        logger.info('反向用例输入完成')
        handler[1].sleep(1)
        assert handler[1].is_toast_show(data['error_msg'])
        handler[1].save_picture(data['name'])
