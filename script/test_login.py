#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/2 18:25
#文件: test_login..PY
#工具：PyCharm Community Edition
import unittest,logging,requests
from api.login_api import LoginApi
from utils import assert_common_utils

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api=LoginApi()
    def tearDown(self):
        pass
    #登录成功用例
    def test01_login_success(self):
        requests = self.login_api.login_params({"mobile":"13800000002",
                                                "password":"123456"})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self,requests,200,True,10000,'操作成功')
    #测试用户名不存在
    def test02_username_is_not_exist(self):
        requests = self.login_api.login_params({"mobile": "13400002",
                                                "password": "12356"})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, False, 20001, '用户名或密码错误')
    #测试密码错误
    def test03_password_is_error(self):
        requests = self.login_api.login_params({"mobile": "13400000002",
                                                "password": "1234256"})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, False, 20001, '用户名或密码错误')
    #测试无参
    def test04_none_params(self):
        requests = self.login_api.login_params({})
        logging.info("4登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, False, 20001, '用户名或密码错误')
    #用户名为空
    def test05_username_is_null(self):
        requests = self.login_api.login_params({"mobile": "",
                                                "password": "1234256"})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, False, 20001, '用户名或密码错误')
    #密码为空
    def test06_password_is_empty(self):
        requests = self.login_api.login_params({"mobile": "13400000002",
                                                "password": ""})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, False, 20001, '用户名或密码错误')
    #少参:mobile
    def test07_less_mobile(self):
        requests = self.login_api.login_params({"password": "123456"})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, False, 20001, '用户名或密码错误')
    def test08_less_password(self):
        requests = self.login_api.login_params({"mobile": "13400000002"})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, False, 20001, '用户名或密码错误')
    #多参
    def test09_add_params(self):
        requests = self.login_api.login_params({"mobile": "13400000002",
                                                "password": "123456",
                                               "code":"23434"})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, True, 10000, "操作成功")
    #错误参数
    def test10_error_params(self):
        requests = self.login_api.login_params({"mobile": "13400000002",
                                               "passord": "123456"})
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self, requests, 200, False, 20001, "用户名或密码错误")
