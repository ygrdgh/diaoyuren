# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 11:53
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : data_for_login.py
# @Software: PyCharm

success_data = {'name': '正常登录', 'username': '18843010983', 'password': 'ipmnlfof123'}
failed_data = [{'name': '反向用例-用户名为空', 'username': '', 'password': 'ipmnlfiof', 'error_msg': '用户名不能为空'},
    {'name': '反向用例-用户名错误-密码正确', 'username': 'plkjf才有', 'password': 'ipmnlfiof', 'error_msg': '用户名不存在'},
    {'name': '反向用例-密码为空', 'username': '18843010983', 'password': '', 'error_msg': '密码不能为空'},
    {'name': '反向用例-用户名正确-密码错误', 'username': '18843010983', 'password': 'ipmnl', 'error_msg': '账号或密码错误'}]