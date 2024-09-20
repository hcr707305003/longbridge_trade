from flask import Blueprint, jsonify, current_app
from utils.trade import Trade
import utils.config as config
import utils.tools as tools

# 创建 API 的蓝图
api_route = Blueprint('api', __name__)

# 提交订单
@api_route.route('/submit_order')
def submit_order():
    print(Trade(config.long_bridge_config).submit())
    return tools.to_json()

# 取消订单
@api_route.route('/cancel_order/<order_id>')
def cancel_order(order_id):
    Trade(config.long_bridge_config).cancel(order_id)
    return tools.to_json()

# 获取今日订单
@api_route.route('/today_order')
def today_order():
    return tools.to_json(Trade(config.long_bridge_config).today_order_list())

# 获取历史订单
@api_route.route('/history_order')
def history_order():
    return tools.to_json(Trade(config.long_bridge_config).history_order_list())

# 获取操作记录
@api_route.route('/today_execution')
def today_execution():
    return tools.to_json(Trade(config.long_bridge_config).today_execution_list())

# 获取历史操作记录
@api_route.route('/history_execution')
def history_execution():
    return tools.to_json(Trade(config.long_bridge_config).history_execution_list())