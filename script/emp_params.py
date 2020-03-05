#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/3 11:53
#文件: emp_params.PY
#工具：PyCharm Community Edition
import app
import unittest
import logging
from utils import assert_common_utils,DBUtils,emp_data
from api.emp_api import EmployeeApi
from parameterized import parameterized
from app import BASE_DIR

all_list=emp_data(BASE_DIR+'/data/emp.json')
add_list=[]
query_list=[]
modify_list=[]
dele_list = []
add_list.append(all_list[0])
query_list.append(all_list[1])
modify_list.append(all_list[2])
dele_list.append(all_list[3])

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
    @parameterized.expand(add_list)
    def test02_add_emp(self,username,mobile,start_code,success,code,masge):
        response_add_emp = self.employee_api.add_emp(username,mobile,app.HEADERS)
        logging.info("添加员工后的接口结果为：{}".format(response_add_emp.json()))
        assert_common_utils(self, response_add_emp, start_code, success, code, masge)
        emp_id = response_add_emp.json().get('data').get('id')
        app.EMPID =emp_id
        #查询
    @parameterized.expand(query_list)
    def test03_query_emp(self,start_code,success,code,masge):
        response_query = self.employee_api.query_emp(app.EMPID,app.HEADERS)
        logging.info("查询搜索员工的结果为：{}".format(response_query.json()))
        assert_common_utils(self, response_query, start_code, success, code, masge)
        #修改
    @parameterized.expand(modify_list)
    def test04_modify_emp(self,username,start_code,success,code,masge):
        response_modify = self.employee_api.addup_emp(username,app.EMPID,app.HEADERS)
        logging.info("查询修改员工的结果为：{}".format(response_modify.json()))
        with DBUtils() as db:
            #执行SQL语句
            sql = "SELECT username FROM `bs_user` where id={}".format(app.EMPID)
            db.execute(sql)
            result = db.fetchone()
            logging.info("sql查询结果为：{}".format(result))
            #断言
            self.assertEqual(username,result[0])


        assert_common_utils(self,response_modify, start_code, success, code, masge)
        #删除
    @parameterized.expand(dele_list)
    def test05_delete_emp(self,start_code,success,code,masge):
        response_delete = self.employee_api.did_emp(app.EMPID,app.HEADERS)
        logging.info("查询删除员工的结果为：{}".format(response_delete.json()))
        assert_common_utils(self,response_delete,start_code,success,code,masge)