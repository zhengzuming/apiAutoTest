#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/1 16:40
#文件: __init__.PY
#工具：PyCharm Community Edition
import app
import logging
#初始化日志
app.init_log_config()
#测试
logging.info("测试日志是否能够正常打印2！")