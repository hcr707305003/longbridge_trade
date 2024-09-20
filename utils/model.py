from datetime import datetime, date
from decimal import Decimal

class OrderModel:
    def __init__(self, order):
        self.order = order

    def to_dict(self):
        return {
            "order_id": self.order.order_id,
            "status": str(self.order.status),
            "stock_name": self.order.stock_name,
            "quantity": self.order.quantity,
            "executed_quantity": self.order.executed_quantity,
            "price": float(self.order.price) if isinstance(self.order.price, Decimal) else self.order.price,
            "executed_price": float(self.order.executed_price) if isinstance(self.order.executed_price, Decimal) else self.order.executed_price,
            "submitted_at": self.order.submitted_at.isoformat() if isinstance(self.order.submitted_at, (datetime, date)) else self.order.submitted_at,
            "side": str(self.order.side),
            "symbol": self.order.symbol,
            "order_type": str(self.order.order_type),
            "last_done": self.order.last_done,
            "trigger_price": self.order.trigger_price,
            "msg": self.order.msg,
            "tag": str(self.order.tag),
            "time_in_force": str(self.order.time_in_force),
            "expire_date": self.order.expire_date.isoformat() if isinstance(self.order.expire_date, (datetime, date)) else self.order.expire_date,
            "updated_at": self.order.updated_at.isoformat() if isinstance(self.order.updated_at, (datetime, date)) else self.order.updated_at,
            "trigger_at": self.order.trigger_at,
            "trailing_amount": self.order.trailing_amount,
            "trailing_percent": self.order.trailing_percent,
            "limit_offset": self.order.limit_offset,
            "trigger_status": self.order.trigger_status,
            "currency": self.order.currency,
            "outside_rth": str(self.order.outside_rth),
            "remark": self.order.remark
        }
    
class ExecutionModel:
    def __init__(self, execution):
        self.execution = execution

    def to_dict(self):
        return {
            "trade_id": self.execution.trade_id,
            "order_id": self.execution.order_id,
            "symbol": self.execution.symbol,
            "trade_done_at": self.execution.trade_done_at.isoformat() if isinstance(self.execution.trade_done_at, (datetime, date)) else self.execution.trade_done_at,
            "quantity": self.execution.quantity,
            "price": float(self.execution.price) if isinstance(self.execution.price, Decimal) else self.execution.price,
        }