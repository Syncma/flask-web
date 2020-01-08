from app.api import bp
from flask import request
from app.models import User
from app import db
from app.api.auth import basic_auth, token_auth
from app.auth.forms import LoginForm
from app.api.status import bad_request, success_request
from app.serializers import user_schema


# 在视图中使用蓝图
@bp.route('/', methods=['GET'])
def index():
    return "<h1>这是前台页面</h1>"


# 创建用户
@bp.route("/users", methods=['POST'])
def create_user():
    form = LoginForm(request.form)

    if form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        data = {"username": username, "email": email, 'password': password}

        # flask-sqlalchemy默认开启了事务
        user = User()
        user.set_password(data['password'])
        user.from_dict(data)

        try:
            db.session.add(user)
            db.session.commit()  # 事务提交

        except:
            db.session.rollback()  # 事务回滚

        # 返回值
        user_dict = user_schema.dump(user)
        return success_request(user_dict)

    else:
        error = form.errors
        return bad_request(error)


# 登录
@bp.route("/login", methods=['GET'])
@basic_auth.login_required
def login_user():

    return "Hello, %s!" % basic_auth.username()