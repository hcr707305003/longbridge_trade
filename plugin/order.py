from decimal import Decimal
from longport.openapi import TradeContext, OrderSide, OrderType, TimeInForceType
from model import (
    OrderModel
)

class Order:
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

    def order_list(self):
        """
        获取订单列表
        """
        return [OrderModel(order).to_dict() for order in self.trade_ctx.today_orders()]