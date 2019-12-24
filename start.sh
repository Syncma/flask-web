#!/bin/sh

export FLASK_APP=run.py

#默认端口是5000,可以进行配置
export FLASK_RUN_PORT=8000

flask run