from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from flask_json import json_response


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['data'] = message
    payload['message'] = "操作失败，请稍后重试"
    response = jsonify(payload)
    response.status_code = status_code

    return json_response(code=status_code,
                         message=payload['message'],
                         data=payload['data'])


def bad_request(message):
    return error_response(400, message)


def success_response(status_code, data=None):
    SuccessMsg = "操作成功"
    return json_response(code=status_code, message=SuccessMsg, data=data)


def success_request(message):
    return success_response(200, message)