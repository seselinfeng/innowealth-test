# coding:utf-8

from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from logging.handlers import TimedRotatingFileHandler
from os import path
import time
import redis
import logging

# 数据库
db = SQLAlchemy()
# 创建redis连接对象
redis_store = None

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logs/%s.log' % time.strftime('%Y_%m_%d'))

# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小，保存的日志文件个数上限
file_log_handler = TimedRotatingFileHandler(log_file_path, when='D', interval=1, backupCount=10)

# 创建日志记录的格式
formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

# 为日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)

# 为全局的日志工具对象，添加记录器
logging.getLogger().addHandler(file_log_handler)


# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name:str 配置模式的模式名字（'develop','product')
    :rtype: object
    """
    app = Flask(__name__)
    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    # 初始化数据库
    db.init_app(app)
    global redis_store
    # redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    Session(app)

    # 为flask补充csrf防护
    CSRFProtect(app)

    # 注册蓝图(解决和db循环导入问题）
    from innowealth import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix='/api/v1.0')

    return app
