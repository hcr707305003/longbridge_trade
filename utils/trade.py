from decimal import Decimal
from longport.openapi import TradeContext, OrderSide, OrderType, TimeInForceType
from utils.model import (
    OrderModel,
    ExecutionModel,
    AccountBalanceModel,
    CashFlowModel,
    FundPositionsResponseModel,
    MarginRatioModel,
    StockPositionsResponseModel
)

class Trade:
    def __init__(self, config):
        self.config = config
        self.trade_ctx = TradeContext(self.config)

    def account_balance(self, currency="HKD"):
        """
        账户余额
        """
        return [AccountBalanceModel(balance).to_dict() for balance in self.trade_ctx.account_balance(
            currency=currency,
        )]

    def cash_flow(self, start_time, end_time):
        """
        资金流水
        """
        return [CashFlowModel(cash).to_dict() for cash in self.trade_ctx.cash_flow(
            start_at=start_time,
            end_at=end_time
        )]

    def fund_positions(self):
        """
        获取基金持仓
        """
        return FundPositionsResponseModel(self.trade_ctx.fund_positions()).to_dict()
    
    def margin_ratio(self, symbol = "700.HK"):
        """
        获取保证金比例
        """
        return MarginRatioModel(self.trade_ctx.margin_ratio(symbol)).to_dict()

    def stock_positions(self):
        """
        股票持仓
        """
        return StockPositionsResponseModel(self.trade_ctx.stock_positions()).to_dict()

    def submit_order(self):
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

    
    def modify_order(self, order_id, quantity, price):
        """
        修改订单
        """
        resp = self.trade_ctx.replace_order(
            order_id=order_id,
            quantity=quantity,
            price=price
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
    
    def order_detail(self, order_id):
        """
        获取订单详情
        """
        return OrderModel(self.trade_ctx.order_detail(order_id)).to_dict()

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