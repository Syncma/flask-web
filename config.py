import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:Qian123#@localhost:3306/test?charset=utf8"
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_ADD_STATUS = False  #这是给json_response模块用的
