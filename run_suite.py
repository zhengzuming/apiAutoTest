#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/1 16:40
#文件: run_suite.PY
#工具：PyCharm Community Edition
from HTMLTestRunner_PY3 import HTMLTestRunner
from app import BASE_DIR
import unittest,time
from script.test_params import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
# report_path = BASE_DIR+"/report/ihrt{}.html".format(time.strftime('%Y%m%d %H%M%S'))
#如果要在jenkins当中引入这个报告，那么需要把时间戳删掉
report_path = BASE_DIR+"/report/ihrt.html"
with open(report_path,mode='wb') as f:
    runner = HTMLTestRunner(f,verbosity=2,title="ihtl登录接口测试",description="生成报告，更美观")
    runner.run(suite)
