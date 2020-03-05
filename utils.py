#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/1 16:39
#文件: utils.PY
#工具：PyCharm Community Edition
#封装通用断言函数
import pymysql,json
from app import BASE_DIR

def assert_common_utils(self,response,http_code,success,code,message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get('success'))
    self.assertEqual(code, response.json().get('code'))
    self.assertIn(message, response.json().get('message'))
#封装数据库
class DBUtils:
    #初始化类时，要运行代码
    def __init__(self,host="182.92.81.159",user="readuser",passeord='iHRM_user_2019',databaser='ihrm'):
        self.host=host
        self.user=user
        self.password=passeord
        self.database=databaser
    #代表使用with语法时，进入函数时会先运行enter的代码
    def __enter__(self):
        self.coon=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        self.cusor=self.coon.cursor()
        return self.cusor
    #代表退出with语句块时，会运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        #关闭游标和关闭连接
        if self.cusor:
            self.cusor.close()
        if self.coon:
            self.coon.close()

def read_login_data(login_data_path):
    with open(login_data_path,mode='r',encoding="utf-8") as f:
        jsonData = json.load(f)
        all_list=[]
        for case_data in jsonData:
            result_list=[]
            for in_case in case_data.values():
                result_list.append(in_case)
            all_list.append(tuple(result_list))

    print("读取出来的数据为：",all_list)
    return all_list
def emp_data(login_data_path):
    with open(login_data_path,mode='r',encoding="utf-8") as f:
        jsonData = json.load(f)
        all_list=[]
        for case_data in jsonData.values():
            result_list=[]
            for in_case in case_data.values():
                result_list.append(in_case)
            result_list.pop(0)
            all_list.append(tuple(result_list))
    print("读取出来的数据为：",all_list)
    return all_list
if __name__ == "__main__":
    emp_data(BASE_DIR+"/data/emp.json")


