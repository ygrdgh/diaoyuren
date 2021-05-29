# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 21:05
# @Author  : Yan
# @Email   : 18843010983@163.com
# @File    : get_config.py
# @Software: PyCharm

import os
import configparser
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def read_config(config_file_path, filed, key):
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file_path, encoding='utf-8')
        if sys.platform == 'win32':
            result = cf.get(filed, key).replace('base_dir', str(BASE_DIR)).replace('/', '\\')

        else:
            result = cf.get(filed, key).replace('base_dir', str(BASE_DIR))


    except Exception as e:
        print(e)
        sys.exit(1)

    return result
