# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 20:49
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : test_log.py
# @Software: PyCharm

import  logging

logging.basicConfig(level=logging.ERROR)
logging.debug('this is a debug log')
logging.info('this is a info log')
logging.warning('this is a waring log')
logging.error('this is a error log')
logging.critical('this is a critical log')