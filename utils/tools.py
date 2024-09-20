import json

def to_json(data = None, msg = 'success', code = 0):
    return json.dumps({
        'msg': msg,
        'code': code,
        'data': data
    })