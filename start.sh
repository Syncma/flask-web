#!/bin/sh

export FLASK_APP=run.py

#默认端口是5000,可以进行配置
export FLASK_RUN_PORT=8000

#开启debug模式
# export FLASK_DEBUG=1

#环境：1表示testing环境, 2表示dev环境
export APP_ENV=1

flask run
