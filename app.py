#_*_coding: UTF-8_*_
#ID:  Administrator
#日期：2020/3/1 16:39
#文件: app.py.PY
#工具：PyCharm Community Edition
#初始化日志配置
import os,logging
from logging import handlers
#定义两个在脚本中使用的全局变量
HEADERS = {}
EMPID = ""
#获取当前项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def init_log_config():
    #创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    #创建控制台处理器
    sh = logging.StreamHandler()
    #创建文件处理器
    log_path=BASE_DIR + "/log/demo.log"
    fh = handlers.TimedRotatingFileHandler(log_path,when="s",interval=10,backupCount=2,encoding="utf-8")
    #创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s][%(filename)s(%(funcName)s:%(lineno)d)] -%(message)s'
    formatter = logging.Formatter(fmt)
    #将格式器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)
if __name__=="__main__":
    #初始化日志配置时，由于没有返回日志器，所以这个配置函数中的全部
    #配置都会配置到logging的root节点
    init_log_config()
    #既然初始化到了root节点，那么我们可以直接使用logging模块打印日志
    logging.info("测试日志不会打印")


