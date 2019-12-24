from app.api import bp
from flask import jsonify, request
from app.models import User
from app import db
from flask_json import json_response
from app.api.auth import basic_auth, token_auth


#在视图中使用蓝图
@bp.route('/', methods=['GET'])
def index():
    return "<h1>这是前台页面</h1>"


#创建用户
@bp.route("/users", methods=['POST'])
def create_user():
    username = request.form.get('username', '', type=str)
    email = request.form.get('email', '', type=str)
    password = request.form.get('password', '', type=str)

    data = {"username": username, "email": email, 'password': password}

    #flask-sqlalchemy默认开启了事务
    user = User()
    user.set_password(data['password'])
    user.from_dict(data)

    try:
        db.session.add(user)
        db.session.commit()  #事务提交

    except:
        db.session.rollback()  #事务回滚

    #返回值
    response = jsonify(user.to_dict())
    return json_response(code=response.status_code, data=user.to_dict())


#登录
@bp.route("/login", methods=['GET'])
@basic_auth.login_required
def login_user():

    return "Hello, %s!" % basic_auth.username()