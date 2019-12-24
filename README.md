# flask-web

flask web example

# 说明
基于flask框架开发的一个web api


# 项目主要结构
```
├── app
│   ├── api
│   │   ├── errors.py   -定义API错误返回格式
│   │   ├── __init__.py
│   │   └── users.py    -路由
│   ├── auth
│   │   └── __init__.py -鉴权功能
│   ├── errors
│   │   ├── handlers.py -定义web错误返回格式
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models.py       -表设计
│   ├── static          -静态文件目录
│   └── templates       -模板目录
├── config.py           -配置文件
├── deployment          -部署
│   └── supervisor
│       └── app.conf
├── logs                -日志目录（如果没有，系统会自动创建）
├── README.md
├── requirement.txt     -依赖包
├── run.py              -主程序
├── start.sh            -运行脚本
└── tests               -测试用例目录

```

# 运行环境
python 3.6.7


# 功能说明
```
    简单web服务
    对想要熟悉flask 应用的人有帮助
```
# 安装步骤
## 1.安装依赖模块
```
pip install -r requirement.txt
```

## 2.初始化数据表信息（**注意:数据库需要手动创建**）

```
命令顺序是： 
flask db init   #创建新的迁移存储库
flask db migrate   #生成一个新的修订版本
flask db upgrade    #创建到数据库
```

### 具体操作步骤：
```
[jian@laptop apiserver]$ pwd
/home/jian/prj/python/apiserver

[jian@laptop apiserver]$ flask db init
  Creating directory /home/jian/prj/python/apiserver/migrations ...  done
  Creating directory /home/jian/prj/python/apiserver/migrations/versions ...  done
  Generating /home/jian/prj/python/apiserver/migrations/alembic.ini ...  done
  Generating /home/jian/prj/python/apiserver/migrations/env.py ...  done
  Generating /home/jian/prj/python/apiserver/migrations/script.py.mako ...  done
  Generating /home/jian/prj/python/apiserver/migrations/README ...  done
  Please edit configuration/connection/logging settings in
  '/home/jian/prj/python/apiserver/migrations/alembic.ini' before proceeding.

[jian@laptop apiserver]$ flask db migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
  Generating /home/jian/prj/python/apiserver/migrations/versions/20f73d9e757e_.py
  ...  done
[jian@laptop apiserver]$ flask db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 20f73d9e757e, empty message

```
### 这些命令的含义可以查看
```
https://www.jianshu.com/p/4b9740551f5c
```


### 3.启动服务

```
sh start.sh
```


### 4.gunicorn 启动方式
```
[jian@laptop apiserver]$ pwd
/home/jian/prj/python/apiserver

[jian@laptop apiserver]$ gunicorn -b localhost:8000 -w 2 run:app
#其中： 第一个 run 指的是 run.py 文件； 
第二个指的是 flask 应用的名字，app = Flask(name)
-w 为开启n个进程
```



### 5.待办事宜 Todo 列表

- [ ] 用户鉴权
- [ ] 用户界面
- [ ] docker