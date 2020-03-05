#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/2 17:54
#文件: test_emp01.PY
#工具：PyCharm Community Edition
import app
import unittest
import logging
from utils import assert_common_utils,DBUtils
from api.emp_api import EmployeeApi
import pymysql

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee_api = EmployeeApi()
    def tearDown(self):
        pass
    def test01_login_success(self):
        #登录
        response = self.employee_api.login("13800000002","123456")
        logging.info("员工模块的登录结果为：{}".format(response.json()))
        token = "Bearer " + response.json().get("data")
        logging.info("取出的令牌为：{}".format(token))
        headers = {"Content-Type":"application/json","Authorization":token}
        app.HEADERS = headers
        logging.info("员工模块请求头为：{}".format(app.HEADERS))
        #添加
    def test02_add_emp(self):
        response_add_emp = self.employee_api.add_emp("雪山银燕sdf",'14225567432',app.HEADERS)
        logging.info("添加员工后的接口结果为：{}".format(response_add_emp.json()))
        assert_common_utils(self, response_add_emp, 200, True, 10000, '操作成功')
        emp_id = response_add_emp.json().get('data').get('id')
        app.EMPID =emp_id
        #查询
    def test03_query_emp(self):
        response_query = self.employee_api.query_emp(app.EMPID,app.HEADERS)
        logging.info("查询搜索员工的结果为：{}".format(response_query.json()))
        assert_common_utils(self, response_query, 200, True, 10000, '操作成功')
        #修改
    def test04_modify_emp(self):
        response_modify = self.employee_api.addup_emp("俏如来",app.EMPID,app.HEADERS)
        logging.info("查询修改员工的结果为：{}".format(response_modify.json()))
        with DBUtils() as db:
            #执行SQL语句
            sql = "SELECT username FROM `bs_user` where id={}".format(app.EMPID)
            db.execute(sql)
            result = db.fetchone()
            logging.info("sql查询结果为：{}".format(result))
            #断言
            self.assertEqual("俏如来",result[0])


        assert_common_utils(self,response_modify, 200, True, 10000, '操作成功')
        #删除
    def test05_delete_emp(self):
        response_delete = self.employee_api.did_emp(app.EMPID,app.HEADERS)
        logging.info("查询删除员工的结果为：{}".format(response_delete.json()))
        assert_common_utils(self,response_delete,200,True,10000,'操作成功')