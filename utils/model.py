from datetime import datetime, date
from decimal import Decimal

class OrderModel:
    def __init__(self, order):
        self.order = order

    def to_dict(self):
        data = {
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
            "last_done": float(self.order.last_done) if isinstance(self.order.last_done, Decimal) else self.order.last_done,
            "trigger_price": float(self.order.trigger_price) if isinstance(self.order.trigger_price, Decimal) else self.order.trigger_price,
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
        if hasattr(self.order, 'free_status'):
            data['free_status'] = str(self.order.free_status)

        if hasattr(self.order, 'free_amount'):
            data['free_amount'] = 0 if self.order.free_amount is None else (float(self.order.free_amount) if isinstance(self.order.free_amount, Decimal) else self.order.free_amount),
            
        if hasattr(self.order, 'free_currency'):
            data['free_currency'] = str(self.order.free_currency)
            
        if hasattr(self.order, 'deductions_status'):
            data['deductions_status'] = str(self.order.deductions_status)
            
        if hasattr(self.order, 'deductions_amount'):
            data['deductions_amount'] = str(self.order.deductions_amount)
            
        if hasattr(self.order, 'deductions_currency'):
            data['deductions_currency'] = str(self.order.deductions_currency)
            
        if hasattr(self.order, 'platform_deducted_status'):
            data['platform_deducted_status'] = str(self.order.platform_deducted_status)
            
        if hasattr(self.order, 'platform_deducted_amount'):
            data['platform_deducted_amount'] = str(self.order.platform_deducted_amount)
            
        if hasattr(self.order, 'platform_deducted_currency'):
            data['platform_deducted_currency'] = str(self.order.platform_deducted_currency)
            
        if hasattr(self.order, 'history'):
            data['history'] = [OrderHistoryDetailsModel(h).to_dict() for h in self.order.history]
        
        if hasattr(self.order, 'charge_detail'):
            data['charge_detail'] = OrderChargeDetailModel(self.order.charge_detail).to_dict()
            
        

        return data

class OrderHistoryDetailsModel:

    def __init__(self, history):
        self.history = history

    def to_dict(self):
        return {
            "price": float(self.history.price) if isinstance(self.history.price, Decimal) else self.history.price,
            'quantity': float(self.history.quantity) if isinstance(self.history.quantity, Decimal) else self.history.quantity,
            "status": str(self.history.status),
            "msg": self.history.msg,
            "time": self.history.time.isoformat() if isinstance(self.history.time, (datetime, date)) else self.history.time,
        }
    
class OrderChargeDetailModel:
    def __init__(self, charge_detail):
        self.charge_detail = charge_detail

    def to_dict(self):
        return {
            "total_amount": float(self.charge_detail.total_amount) if isinstance(self.charge_detail.total_amount, Decimal) else self.charge_detail.total_amount,
            "currency": self.charge_detail.currency,
            # "items": [OrderChargeItemModel(item).to_dict() for item in self.charge_detail.items],
        }
    
class OrderChargeItemModel:
    def __init__(self, item):
        self.item = item

    def to_dict(self):
        return {
            "code": str(self.item.code),
            "name": self.item.name,
            "fees": [OrderChargeFeesModel(fee).to_dict() for fee in self.item.fees],
        }
    
class OrderChargeFeesModel:
    def __init__(self, fees):
        self.fees = fees

    def to_dict(self):
        return {
            "code": str(self.fees.code),
            "name": self.fees.name,
            "amount": float(self.fees.amount) if isinstance(self.fees.amount, Decimal) else self.fees.amount,
            "currency": self.fees.currency,
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
    
class CashModel:
    def __init__(self, cash):
        self.cash = cash

    def to_dict(self):
        return {
            "withdraw_cash": float(self.cash.withdraw_cash) if isinstance(self.cash.withdraw_cash, Decimal) else self.cash.withdraw_cash,
            "available_cash": float(self.cash.available_cash) if isinstance(self.cash.available_cash, Decimal) else self.cash.available_cash,
            "frozen_cash": float(self.cash.frozen_cash) if isinstance(self.cash.frozen_cash, Decimal) else self.cash.frozen_cash,
            "settling_cash": float(self.cash.settling_cash) if isinstance(self.cash.settling_cash, Decimal) else self.cash.settling_cash,
            "currency": self.cash.currency
        }
    
class AccountBalanceModel:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def to_dict(self):
        return {
            "total_cash": float(self.account_balance.total_cash) if isinstance(self.account_balance.total_cash, Decimal) else self.account_balance.total_cash,
            "max_finance_amount": float(self.account_balance.max_finance_amount) if isinstance(self.account_balance.max_finance_amount, Decimal) else self.account_balance.max_finance_amount,
            "remaining_finance_amount": float(self.account_balance.remaining_finance_amount) if isinstance(self.account_balance.remaining_finance_amount, Decimal) else self.account_balance.remaining_finance_amount,
            "risk_level": self.account_balance.risk_level,
            "margin_call": float(self.account_balance.margin_call) if isinstance(self.account_balance.margin_call, Decimal) else self.account_balance.margin_call,
            "currency": self.account_balance.currency,
            "cash_infos": [CashModel(cash).to_dict() for cash in self.account_balance.cash_infos],
            "net_assets": float(self.account_balance.net_assets) if isinstance(self.account_balance.net_assets, Decimal) else self.account_balance.net_assets,
            "init_margin": float(self.account_balance.init_margin) if isinstance(self.account_balance.init_margin, Decimal) else self.account_balance.init_margin,
            "maintenance_margin": float(self.account_balance.maintenance_margin) if isinstance(self.account_balance.maintenance_margin, Decimal) else self.account_balance.maintenance_margin,
            "buy_power": float(self.account_balance.buy_power) if isinstance(self.account_balance.buy_power, Decimal) else self.account_balance.buy_power
        }
    
class CashFlowModel:
    def __init__(self, cash_flow):
        self.cash_flow = cash_flow

    def to_dict(self):
        return {
            'transaction_flow_name': self.cash_flow.transaction_flow_name,
            'direction': str(self.cash_flow.direction),
            'business_type': str(self.cash_flow.business_type),
            'balance': float(self.cash_flow.balance) if isinstance(self.cash_flow.balance, Decimal) else self.cash_flow.balance,
            'currency': self.cash_flow.currency,
            "business_time": self.cash_flow.business_time.isoformat() if isinstance(self.cash_flow.business_time, (datetime, date)) else self.cash_flow.business_time,
            'symbol': self.cash_flow.symbol,
            'description': self.cash_flow.description
        }

class FundPositionsResponseModel:
    def __init__(self, fund_position):
        self.fund_position = fund_position

    def to_dict(self):
        return {
            'channels': [FundPositionChannelModel(channel).to_dict() for channel in self.fund_position.channels],
        }

class FundPositionChannelModel:
    def __init__(self, fund_position_channel):
        self.fund_position_channel = fund_position_channel
    
    def to_dict(self):
        return {
            'account_channel': self.fund_position_channel.account_channel,
            'positions': [FundPositionModel(position).to_dict() for position in self.fund_position_channel.positions]
        }
        
    
class FundPositionModel:
    def __init__(self, fund_position):
        self.fund_position = fund_position

    def to_dict(self):
        return {
            'symbol': self.fund_position.symbol,
            'current_net_asset_value': float(self.fund_position.current_net_asset_value) if isinstance(self.fund_position.current_net_asset_value, Decimal) else self.fund_position.current_net_asset_value,
            "net_asset_value_day": self.fund_position.net_asset_value_day.isoformat() if isinstance(self.fund_position.net_asset_value_day, (datetime, date)) else self.fund_position.net_asset_value_day,
            'symbol_name': self.fund_position.symbol_name,
            'currency': self.fund_position.currency,
            'cost_net_asset_value': float(self.fund_position.cost_net_asset_value) if isinstance(self.fund_position.cost_net_asset_value, Decimal) else self.fund_position.cost_net_asset_value,
            'holding_units': float(self.fund_position.holding_units) if isinstance(self.fund_position.holding_units, Decimal) else self.fund_position.holding_units,
        }
    
class MarginRatioModel:
    def __init__(self, margin_ratio):
        self.margin_ratio = margin_ratio

    def to_dict(self):
        return {
            'im_factor': float(self.margin_ratio.im_factor) if isinstance(self.margin_ratio.im_factor, Decimal) else self.margin_ratio.im_factor,
            'mm_factor': float(self.margin_ratio.mm_factor) if isinstance(self.margin_ratio.mm_factor, Decimal) else self.margin_ratio.mm_factor,
            'fm_factor': float(self.margin_ratio.fm_factor) if isinstance(self.margin_ratio.fm_factor, Decimal) else self.margin_ratio.fm_factor,
        }
    
class StockPositionsResponseModel:
    def __init__(self, stock_position):
        self.stock_position = stock_position

    def to_dict(self):
        return {
            'channels': [StockPositionChannelModel(channel).to_dict() for channel in self.stock_position.channels],
        }

class StockPositionChannelModel:
    def __init__(self, stock_position_channel):
        self.stock_position_channel = stock_position_channel

    def to_dict(self):
        return {
            'account_channel': self.stock_position_channel.account_channel,
            'positions': [StockPositionModel(position).to_dict() for position in self.stock_position_channel.positions]
        }
            

class StockPositionModel:
    def __init__(self, stock_position):
        self.stock_position = stock_position

    def to_dict(self):
        return {
            'symbol': self.stock_position.symbol,
            'symbol_name': self.stock_position.symbol_name,
            'quantity': float(self.stock_position.quantity) if isinstance(self.stock_position.quantity, Decimal) else self.stock_position.quantity,
            'available_quantity': float(self.stock_position.available_quantity) if isinstance(self.stock_position.available_quantity, Decimal) else self.stock_position.available_quantity,
            'currency': self.stock_position.currency,
            'cost_price': float(self.stock_position.cost_price) if isinstance(self.stock_position.cost_price, Decimal) else self.stock_position.cost_price,
            'market': str(self.stock_position.market),
            'init_quantity': self.stock_position.init_quantity
        }
