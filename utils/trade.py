from decimal import Decimal
from longport.openapi import TradeContext, OrderSide, OrderType, TimeInForceType
from utils.model import (
    OrderModel,
    ExecutionModel
)

class Trade:
    def __init__(self, config):
        self.config = config
        self.trade_ctx = TradeContext(self.config)
    
    def submit(self):
        """
        提交订单
        """
        resp = self.trade_ctx.submit_order(
            side=OrderSide.Buy,
            symbol="700.HK",
            order_type=OrderType.LO,
            submitted_price=Decimal("50"),
            submitted_quantity=200,
            time_in_force=TimeInForceType.Day,
            remark="Hello from Python SDK",
        )
        print(resp)
    
    def cancel(self, order_id):
        """
        取消订单
        """
        return self.trade_ctx.cancel_order(order_id)

    def today_order_list(self):
        """
        获取今日订单列表
        """
        return [OrderModel(order).to_dict() for order in self.trade_ctx.today_orders()]
    
    def today_execution_list(self):
        """
        获取今日操作记录
        """
        return [ExecutionModel(execution).to_dict() for execution in self.trade_ctx.today_executions()]
    
    def history_order_list(self):
        """
        获取历史订单列表
        """
        return [OrderModel(order).to_dict() for order in self.trade_ctx.history_orders()]
    
    def history_execution_list(self, symbol = None, start_time = None, end_time = None):
        """
        获取历史操作记录
        """
        return [ExecutionModel(execution).to_dict() for execution in self.trade_ctx.history_executions(
            symbol=symbol,
            start_at=start_time,
            end_at=end_time
        )]