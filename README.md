<!-- TOC -->

- [说明](#说明)
- [项目主要结构](#项目主要结构)
- [运行环境](#运行环境)
- [Windows下安装pyenv环境](#windows下安装pyenv环境)
    - [具体操作步骤如下](#具体操作步骤如下)
        - [1.查看使用的python版本](#1查看使用的python版本)
        - [2.开启办法](#2开启办法)
        - [3.环境](#3环境)
        - [4.退出](#4退出)
- [功能说明](#功能说明)
- [安装步骤](#安装步骤)
    - [1.安装依赖模块](#1安装依赖模块)
    - [2.初始化数据表信息](#2初始化数据表信息)
    - [3.具体操作步骤](#3具体操作步骤)
    - [4.这些命令的含义可以查看](#4这些命令的含义可以查看)
    - [5.启动服务](#5启动服务)
    - [6.gunicorn 启动方式](#6gunicorn-启动方式)
- [待办事宜 Todo 列表](#待办事宜-todo-列表)

<!-- /TOC -->


# 说明
基于flask框架开发的一个web api


# 项目主要结构
```
├── app
│   ├── api
│   │   ├── auth.py		-验证
│   │   ├── errors.py	-定义API错误返回格式
│   │   ├── __init__.py
│   │   └── users.py	-路由
│   ├── auth
│   │   ├── forms.py	-表单数据验证
│   │   └── __init__.py
│   ├── __init__.py	
│   └── models.py		-表设计
├── conf				-配置文件
│   ├── dev.ini
│   └── testing.ini
├── config.py		-读取配置
├── deployment		-部署
│   └── supervisor
│       ├── app.conf
│       ├── readme.md
│       └── supervisor.conf
├── README.md	
├── requirement.txt	-依赖包
├── run.py		-主程序
└── start.sh	-运行脚本


```

# 运行环境
python 3.6.7


# Windows下安装pyenv环境


**windows下推荐使用cmder 这个工具**

[Cmder](https://cmder.net/)

## 具体操作步骤如下
### 1.查看使用的python版本

```python
C:\Users\Sync\Downloads\cmder
λ python
Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 


如果你使用的是**python3** 版本，默认是支持虚拟环境
```

### 2.开启办法
```

1.执行下面命令：
C:\Users\Sync\Downloads\cmder
λ python -m venv myenv

-m venv  使用venv模块
myenv  创建一个虚拟环境，名字教myenv

2.会默认在当前目录创建myenv 目录

输入下面的命令来激活虚拟环境：

λ myenv\Scripts\activate.bat


执行完成后会变成这样：
C:\Users\Sync\Downloads\cmder
(myenv) λ

```

### 3.环境
在这个环境里面就可以做任何事情
```python
安装模块
pip install flask

也可以执行相关程序
```

### 4.退出 

```
输入deactivate.bat 命令就回到了普通的环境 
```




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

## 2.初始化数据表信息
**`注意:数据库需要手动创建`**

```
命令顺序是： 
flask db init   #创建新的迁移存储库
flask db migrate   #生成一个新的修订版本
flask db upgrade    #创建到数据库
```

## 3.具体操作步骤
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
## 4.这些命令的含义可以查看
```
https://www.jianshu.com/p/4b9740551f5c
```


## 5.启动服务

```
sh start.sh
```


## 6.gunicorn 启动方式
```
[jian@laptop apiserver]$ pwd
/home/jian/prj/python/apiserver

[jian@laptop apiserver]$ gunicorn -b localhost:8000 -w 2 run:app
其中： 第一个 run 指的是 run.py 文件； 
第二个指的是 flask 应用的名字，app = Flask(name)
-w 为开启n个进程
```



# 待办事宜 Todo 列表

- [x] 用户鉴权-基本验证
- [x] 根据不同环境读取不同配置文件
- [x] supervisor部署
- [ ] 用户界面
- [ ] docker 部署