import json

def to_json(data = None, msg = 'success', code = 0):
    return json.dumps({
        'msg': msg,
        'code': code,
        'data': data
    })

async def db_handle(db, callback):
        await db.connect()
        await callback() # 执行回调函数
        await db.close()