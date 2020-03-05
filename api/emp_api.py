#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/2 15:06
#文件: emp_api.PY
#工具：PyCharm Community Edition

import requests

class EmployeeApi:
    def __init__(self):
        pass
    def login(self,mobile,password):
        login_url="http://182.92.81.159/api/sys/login"
        jsonData = {"mobile":mobile,
                    "password":password}
        return requests.post(login_url,json=jsonData)
    def add_emp(self,username,mobile,headers):
        add_emp_url = "http://182.92.81.159/api/sys/user"
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-03-02"
        }
        return requests.post(add_emp_url,json=jsonData,headers=headers)
    def query_emp(self,emp_id,headers):
        add_emp_url = "http://182.92.81.159/api/sys/user"
        return requests.get(add_emp_url+"/"+emp_id,headers=headers)

    def addup_emp(self,username,emp_id,headers):
        add_emp_url = "http://182.92.81.159/api/sys/user"
        return requests.put(add_emp_url+'/'+emp_id,json={"username":username},headers=headers)
    def did_emp(self,emp_id,headers):
        add_emp_url = "http://182.92.81.159/api/sys/user"
        return requests.delete(add_emp_url+'/'+emp_id,headers=headers)