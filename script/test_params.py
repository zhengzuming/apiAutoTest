#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/3 11:12
#文件: test_params.PY
#工具：PyCharm Community Edition
import unittest,logging
from api.login_api import LoginApi
from utils import assert_common_utils
from parameterized import parameterized
from utils import read_login_data
from app import BASE_DIR

login_data = read_login_data(BASE_DIR+'/data/login.json')
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api=LoginApi()
    def tearDown(self):
        pass
    @parameterized.expand(login_data)
    def test_login_success(self,login,http_code,success,code,message):
        requests = self.login_api.login_params(login)
        logging.info("登陆成功的结果：{}".format(requests.json()))
        assert_common_utils(self,requests,http_code,success,code,message)