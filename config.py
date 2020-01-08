import os
import configparser
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


#检测不同环境读取不同的配置信息
def env_detect():
    env = os.environ.get('APP_ENV', 1)
    if env == "1":
        env = 'TESTING'
    else:
        env = 'DEV'

    return env


def load_config():

    cur_env = env_detect().lower()
    cfgpath = os.path.join(basedir, "conf/%s.ini" % cur_env)

    if os.path.exists(cfgpath):
        CONFIG_PATH = cfgpath

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    host = config["db"]["host"]
    user = config["db"]["user"]
    password = config["db"]["password"]
    port = config["db"]["port"]
    database = config["db"]["database"]

    # Fix bug:ModuleNotFoundError: No module named 'MySQLdb'
    db_url = "mysql+pymysql://{}:{}@{}:{}/{}?".format(user, password, host,
                                                      port, database)

    return "%s" % db_url


class Config(object):

    SQLALCHEMY_DATABASE_URI = load_config()
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_ADD_STATUS = False  #这是给json_response模块用的
