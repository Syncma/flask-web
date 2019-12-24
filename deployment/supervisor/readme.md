# supervisor安装备注

## 模块安装
```python
pip install supervisor
```

## 服务开启

### 配置文件修改
```
修改app.conf里面的directory 项目文件路径

```

### 执行下面命令开启服务

```
[jian@laptop etc]$ tree .
.
├── conf.d
│   └── app.conf
└── supervisor.conf

1 directory, 2 files
[jian@laptop etc]$ pwd
/home/jian/etc

[jian@laptop etc]$ supervisord -c supervisor.conf 

```
### 服务状态查看

```
[jian@laptop prj]$ supervisorctl status
app:app_00                       RUNNING   pid 23696, uptime 0:00:28
```

### 日志
```
配置文件可以进行配置
默认是在/tmp/ 可以查看相应服务日志
```