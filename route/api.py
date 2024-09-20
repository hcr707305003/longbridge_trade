from flask import Blueprint, jsonify, current_app
from plugin.order import Order
import config
import plugin.tools as tools
import json

# 创建 API 的蓝图
api_route = Blueprint('api', __name__)

# 提交订单
@api_route.route('/submit_order')
def submit_order():
    print(Order(config.long_bridge_config).submit())
    return tools.to_json()

# 取消订单
@api_route.route('/cancel_order/<order_id>')
def cancel_order(order_id):
    Order(config.long_bridge_config).cancel(order_id)
    return tools.to_json()

# 获取订单
@api_route.route('/today_order')
def today_order():
    return tools.to_json(Order(config.long_bridge_config).order_list())
