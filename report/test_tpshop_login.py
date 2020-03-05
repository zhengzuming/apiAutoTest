#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/1 16:48
#文件: test_tpshop_login.PY
#工具：PyCharm Community Edition
import requests,unittest
#创建测试类
import time

class TestTpshopLogin(unittest.TestCase):
    #初始化
    def setUp(self)->None:
        self.session = requests.session()
    def tearDown(self)->None:
        self.session.close()
    #创建测试函数