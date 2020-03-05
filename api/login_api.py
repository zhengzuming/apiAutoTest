#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/2 18:23
#文件: login_api.PY
#工具：PyCharm Community Edition
import requests
class LoginApi:
    def __init__(self):
        self.login_url="http://182.92.81.159/api/sys/login"
    #封装能够支持多参、少参、无参、错误参数的测试场景
    def login_params(self,jsonData):
        return requests.post(self.login_url,json=jsonData)