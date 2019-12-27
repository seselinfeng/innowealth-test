# coding:utf-8
import redis


class Config(object):
    """配置信息"""
    SECRET_KEY = 'IN_NO_WEALTH_TEST'

    # 数据库
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'msinfouser'
    PASSWORD = 'msinfouser'
    HOST = '192.168.9.208'
    PORT = 3306
    DATABASE = 'ms_info'

    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                           PORT,
                                                                           DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis
    # REDIS_HOST = '127.0.0.1'
    # REDIS_PORT = 6379

    # flask-session配置
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期


class DevelopmentConfig(Config):
    """开发环境配置类"""
    DEBUG = True


class ProductConfig(Config):
    """生产环境配置类"""
    pass


config_map = {
    'develop': DevelopmentConfig,
    'product': ProductConfig,
}
