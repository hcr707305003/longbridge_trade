from flask import Blueprint, request, jsonify
from utils.trade import Trade
import utils.config as config
import utils.tools as tools
from datetime import datetime, timedelta
from decimal import Decimal

# 创建 API 的蓝图
api_route = Blueprint('api', __name__)

# 提交订单
@api_route.route('/submit_order')
def submit_order():
    print(Trade(config.long_bridge_config).submit_order())
    return tools.to_json()

# 修改订单
@api_route.route('/modify_order/<order_id>')
def modify_order(order_id):
    # 获取查询参数中的开始和结束时间，默认情况下返回一年内的数据
    quantity = request.args.get('quantity')
    if not quantity:
        return tools.to_json(None, '请输入数量', 401)
    else:
        quantity = int(quantity)

    price = Decimal(request.args.get('price'))

    # # 价格不能存在则默认那当前最新价格
    if not price:
        # TODO 获取当前价格
        # price = 
        return tools.to_json(None, '请输入价格', 401)
    else:
        price = Decimal(price)
    Trade(config.long_bridge_config).modify_order(
        order_id,
        quantity,
        price
        )
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

# 订单详情
@api_route.route('/order_detail/<order_id>')
def order_detail(order_id):
    # Trade(config.long_bridge_config).order_detail(order_id)
    return tools.to_json(Trade(config.long_bridge_config).order_detail(order_id))

# 获取操作记录
@api_route.route('/today_execution')
def today_execution():
    return tools.to_json(Trade(config.long_bridge_config).today_execution_list())

# 获取历史操作记录
@api_route.route('/history_execution')
def history_execution():
    return tools.to_json(Trade(config.long_bridge_config).history_execution_list())

# 获取账户余额
@api_route.route('/account_balance')
def account_balance():
    return tools.to_json(Trade(config.long_bridge_config).account_balance())

# 获取资金流水(不传默认返回一年的)
@api_route.route('/cash_flow')
def cash_flow():
    # 获取当前时间
    now = datetime.now()

    # 获取查询参数中的开始和结束时间，默认情况下返回一年内的数据
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    # 如果没有传入开始时间，默认设置为当前时间减去一年
    if not start_time:
        start_time = now - timedelta(days=365)
    else:
        start_time = datetime.strptime(start_time, '%Y-%m-%d')

    # 如果没有传入结束时间，默认设置为当前时间
    if not end_time:
        end_time = now
    else:
        end_time = datetime.strptime(end_time, '%Y-%m-%d')

    return tools.to_json(Trade(config.long_bridge_config).cash_flow(
        start_time=start_time,
        end_time=end_time
    ))

# 获取基金持仓
@api_route.route('/fund_positions')
def fund_positions():
    return tools.to_json(Trade(config.long_bridge_config).fund_positions())

# 获取保证金比例
@api_route.route('/margin_ratio')
def margin_ratio():
    return tools.to_json(Trade(config.long_bridge_config).margin_ratio())

# 获取股票持仓
@api_route.route('/stock_positions')
def stock_positions():
    return tools.to_json(Trade(config.long_bridge_config).stock_positions())