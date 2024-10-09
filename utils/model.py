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

class SecurityModel:
    def __init__(self, security):
        self.security = security
    def to_dict(self):
        return {
            'symbol': self.security.symbol,
            'name_cn': self.security.name_cn,
            'name_en': self.security.name_en,
            'name_hk': self.security.name_hk
        }

class SecurityStaticInfoModel:
    def __init__(self, security_static_info):
        self.security_static_info = security_static_info
    def to_dict(self):
        return {
            'symbol': self.security_static_info.symbol,
            'name_cn': self.security_static_info.name_cn,
            'name_en': self.security_static_info.name_en,
            'name_hk': self.security_static_info.name_hk,
            'exchange': self.security_static_info.exchange,
            'currency': self.security_static_info.currency,
            'lot_size': self.security_static_info.lot_size,
            'total_shares': self.security_static_info.total_shares,
            'circulating_shares': self.security_static_info.circulating_shares,
            'hk_shares': self.security_static_info.hk_shares,
            'eps': float(self.security_static_info.eps) if isinstance(self.security_static_info.eps, Decimal) else self.security_static_info.eps,
            'eps_ttm': float(self.security_static_info.eps_ttm) if isinstance(self.security_static_info.eps_ttm, Decimal) else self.security_static_info.eps_ttm,
            'bps': float(self.security_static_info.bps) if isinstance(self.security_static_info.bps, Decimal) else self.security_static_info.bps,
            'dividend_yield': float(self.security_static_info.dividend_yield) if isinstance(self.security_static_info.dividend_yield, Decimal) else self.security_static_info.dividend_yield,
            'stock_derivatives': [str(stock_derivatives) for stock_derivatives in self.security_static_info.stock_derivatives],
            'board': str(self.security_static_info.board)
        }
    
class SecurityQuoteModel:
    def __init__(self, security_quote):
        self.security_quote = security_quote
    def to_dict(self):
        return {
            'symbol': self.security_quote.symbol,
            'last_done': float(self.security_quote.last_done) if isinstance(self.security_quote.last_done, Decimal) else self.security_quote.last_done,
            'prev_close': float(self.security_quote.prev_close) if isinstance(self.security_quote.prev_close, Decimal) else self.security_quote.prev_close,
            'open': float(self.security_quote.open) if isinstance(self.security_quote.open, Decimal) else self.security_quote.open,
            'high': float(self.security_quote.high) if isinstance(self.security_quote.high, Decimal) else self.security_quote.high,
            'low': float(self.security_quote.low) if isinstance(self.security_quote.low, Decimal) else self.security_quote.low,
            "timestamp": self.security_quote.timestamp.isoformat() if isinstance(self.security_quote.timestamp, (datetime, date)) else self.security_quote.timestamp,
            'volume': self.security_quote.volume,
            'turnover': float(self.security_quote.turnover) if isinstance(self.security_quote.turnover, Decimal) else self.security_quote.turnover,
            'trade_status': str(self.security_quote.trade_status),
            'pre_market_quote': PrePostQuoteModel(self.security_quote.pre_market_quote).to_dict(),
            'post_market_quote': PrePostQuoteModel(self.security_quote.post_market_quote).to_dict(),
            'overnight_quote': self.security_quote.overnight_quote
        }

class PrePostQuoteModel:
    def __init__(self, pre_post_quote):
        self.pre_post_quote = pre_post_quote
    def to_dict(self):
        return {
            'last_done': float(self.pre_post_quote.last_done) if isinstance(self.pre_post_quote.last_done, Decimal) else self.pre_post_quote.last_done,
            "timestamp": self.pre_post_quote.timestamp.isoformat() if isinstance(self.pre_post_quote.timestamp, (datetime, date)) else self.pre_post_quote.timestamp,
            'volume': self.pre_post_quote.volume,
            'turnover': float(self.pre_post_quote.turnover) if isinstance(self.pre_post_quote.turnover, Decimal) else self.pre_post_quote.turnover,
            'high': float(self.pre_post_quote.high) if isinstance(self.pre_post_quote.high, Decimal) else self.pre_post_quote.high,
            'low': float(self.pre_post_quote.low) if isinstance(self.pre_post_quote.low, Decimal) else self.pre_post_quote.low,
            'prev_close': float(self.pre_post_quote.prev_close) if isinstance(self.pre_post_quote.prev_close, Decimal) else self.pre_post_quote.prev_close
        }
    
class TradeModel:
    def __init__(self, trade):
        self.trade = trade
    def to_dict(self):
        return {
            'price': float(self.trade.price) if isinstance(self.trade.price, Decimal) else self.trade.price,
            'volume': self.trade.volume,
            'timestamp': self.trade.timestamp.isoformat() if isinstance(self.trade.timestamp, (datetime, date)) else self.trade.timestamp,
            'trade_type': str(self.trade.trade_type),
            'direction': str(self.trade.direction),
            'trade_session': str(self.trade.trade_session),
        }
    
class CandlestickModel:
    def __init__(self, candlestick):
        self.candlestick = candlestick
    def to_dict(self):
        return {
            'close': float(self.candlestick.close) if isinstance(self.candlestick.close, Decimal) else self.candlestick.close,
            'open': float(self.candlestick.open) if isinstance(self.candlestick.open, Decimal) else self.candlestick.open,
            'low': float(self.candlestick.low) if isinstance(self.candlestick.low, Decimal) else self.candlestick.low,
            'high': float(self.candlestick.high) if isinstance(self.candlestick.high, Decimal) else self.candlestick.high,
            'volume': self.candlestick.volume,
            'turnover': float(self.candlestick.turnover) if isinstance(self.candlestick.turnover, Decimal) else self.candlestick.turnover,
            "timestamp": self.candlestick.timestamp.isoformat() if isinstance(self.candlestick.timestamp, (datetime, date)) else self.candlestick.timestamp
        }

class CapitalFlowLineModel:
    def __init__(self, capital_flow_line):
        self.capital_flow_line = capital_flow_line
    def to_dict(self):
        return {
            'timestamp': self.capital_flow_line.timestamp.isoformat() if isinstance(self.capital_flow_line.timestamp, (datetime, date)) else self.capital_flow_line.timestamp,
            'inflow': float(self.capital_flow_line.inflow) if isinstance(self.capital_flow_line.inflow, Decimal) else self.capital_flow_line.inflow
        }
    
class CapitalDistributionResponseModel:
    def __init__(self, capital_distribution):
        self.capital_distribution = capital_distribution
    def to_dict(self):
        return {
            'timestamp': self.capital_distribution.timestamp.isoformat() if isinstance(self.capital_distribution.timestamp, (datetime, date)) else self.capital_distribution.timestamp,
            'capital_in': CapitalDistributionModel(self.capital_distribution.capital_in).to_dict()
        }
    
class CapitalDistributionModel:
    def __init__(self, capital_distribution):
        self.capital_distribution = capital_distribution
    def to_dict(self):
        return {
            'large': float(self.capital_distribution.large) if isinstance(self.capital_distribution.large, Decimal) else self.capital_distribution.large,
            'medium': float(self.capital_distribution.medium) if isinstance(self.capital_distribution.medium, Decimal) else self.capital_distribution.medium,
            'small': float(self.capital_distribution.small) if isinstance(self.capital_distribution.small, Decimal) else self.capital_distribution.small,
        }
    
class SecurityCalcIndexModel:
    def __init__(self, security_calc_index):
        self.security_calc_index = security_calc_index
    def to_dict(self):
        return {
            'symbol': self.security_calc_index.symbol,
            'last_done': float(self.security_calc_index.last_done) if isinstance(self.security_calc_index.last_done, Decimal) else self.security_calc_index.last_done,
            'change_value': float(self.security_calc_index.change_value) if isinstance(self.security_calc_index.change_value, Decimal) else self.security_calc_index.change_value,
            'change_rate': float(self.security_calc_index.change_rate) if isinstance(self.security_calc_index.change_rate, Decimal) else self.security_calc_index.change_rate,
            'volume': float(self.security_calc_index.volume) if isinstance(self.security_calc_index.volume, Decimal) else self.security_calc_index.volume,
            'turnover': float(self.security_calc_index.turnover) if isinstance(self.security_calc_index.turnover, Decimal) else self.security_calc_index.turnover,
            'ytd_change_rate': float(self.security_calc_index.ytd_change_rate) if isinstance(self.security_calc_index.ytd_change_rate, Decimal) else self.security_calc_index.ytd_change_rate,
            'turnover_rate': float(self.security_calc_index.turnover_rate) if isinstance(self.security_calc_index.turnover_rate, Decimal) else self.security_calc_index.turnover_rate,
            'total_market_value': float(self.security_calc_index.total_market_value) if isinstance(self.security_calc_index.total_market_value, Decimal) else self.security_calc_index.total_market_value,
            'capital_flow': float(self.security_calc_index.capital_flow) if isinstance(self.security_calc_index.capital_flow, Decimal) else self.security_calc_index.capital_flow,
            'amplitude': float(self.security_calc_index.amplitude) if isinstance(self.security_calc_index.amplitude, Decimal) else self.security_calc_index.amplitude,
            'volume_ratio': float(self.security_calc_index.volume_ratio) if isinstance(self.security_calc_index.volume_ratio, Decimal) else self.security_calc_index.volume_ratio,
            'pe_ttm_ratio': float(self.security_calc_index.pe_ttm_ratio) if isinstance(self.security_calc_index.pe_ttm_ratio, Decimal) else self.security_calc_index.pe_ttm_ratio,
            'pb_ratio': float(self.security_calc_index.pb_ratio) if isinstance(self.security_calc_index.pb_ratio, Decimal) else self.security_calc_index.pb_ratio,
            'dividend_ratio_ttm': float(self.security_calc_index.dividend_ratio_ttm) if isinstance(self.security_calc_index.dividend_ratio_ttm, Decimal) else self.security_calc_index.dividend_ratio_ttm,
            'five_day_change_rate': float(self.security_calc_index.five_day_change_rate) if isinstance(self.security_calc_index.five_day_change_rate, Decimal) else self.security_calc_index.five_day_change_rate,
            'ten_day_change_rate': float(self.security_calc_index.ten_day_change_rate) if isinstance(self.security_calc_index.ten_day_change_rate, Decimal) else self.security_calc_index.ten_day_change_rate,
            'half_year_change_rate': float(self.security_calc_index.half_year_change_rate) if isinstance(self.security_calc_index.half_year_change_rate, Decimal) else self.security_calc_index.half_year_change_rate,
            'five_minutes_change_rate': float(self.security_calc_index.five_minutes_change_rate) if isinstance(self.security_calc_index.five_minutes_change_rate, Decimal) else self.security_calc_index.five_minutes_change_rate,
            'expiry_date': float(self.security_calc_index.expiry_date) if isinstance(self.security_calc_index.expiry_date, Decimal) else self.security_calc_index.expiry_date,
            'strike_price': float(self.security_calc_index.strike_price) if isinstance(self.security_calc_index.strike_price, Decimal) else self.security_calc_index.strike_price,
            'upper_strike_price': float(self.security_calc_index.upper_strike_price) if isinstance(self.security_calc_index.upper_strike_price, Decimal) else self.security_calc_index.upper_strike_price,
            'lower_strike_price': float(self.security_calc_index.lower_strike_price) if isinstance(self.security_calc_index.lower_strike_price, Decimal) else self.security_calc_index.lower_strike_price,
            'outstanding_qty': float(self.security_calc_index.outstanding_qty) if isinstance(self.security_calc_index.outstanding_qty, Decimal) else self.security_calc_index.outstanding_qty,
            'outstanding_ratio': float(self.security_calc_index.outstanding_ratio) if isinstance(self.security_calc_index.outstanding_ratio, Decimal) else self.security_calc_index.outstanding_ratio,
            'premium': float(self.security_calc_index.premium) if isinstance(self.security_calc_index.premium, Decimal) else self.security_calc_index.premium,
            'itm_otm': float(self.security_calc_index.itm_otm) if isinstance(self.security_calc_index.itm_otm, Decimal) else self.security_calc_index.itm_otm,
            'implied_volatility': float(self.security_calc_index.implied_volatility) if isinstance(self.security_calc_index.implied_volatility, Decimal) else self.security_calc_index.implied_volatility,
            'warrant_delta': float(self.security_calc_index.warrant_delta) if isinstance(self.security_calc_index.warrant_delta, Decimal) else self.security_calc_index.warrant_delta,
            'call_price': float(self.security_calc_index.call_price) if isinstance(self.security_calc_index.call_price, Decimal) else self.security_calc_index.call_price,
            'to_call_price': float(self.security_calc_index.to_call_price) if isinstance(self.security_calc_index.to_call_price, Decimal) else self.security_calc_index.to_call_price,
            'effective_leverage': float(self.security_calc_index.effective_leverage) if isinstance(self.security_calc_index.effective_leverage, Decimal) else self.security_calc_index.effective_leverage,
            'leverage_ratio': float(self.security_calc_index.leverage_ratio) if isinstance(self.security_calc_index.leverage_ratio, Decimal) else self.security_calc_index.leverage_ratio,
            'conversion_ratio': float(self.security_calc_index.conversion_ratio) if isinstance(self.security_calc_index.conversion_ratio, Decimal) else self.security_calc_index.conversion_ratio,
            'balance_point': float(self.security_calc_index.balance_point) if isinstance(self.security_calc_index.balance_point, Decimal) else self.security_calc_index.balance_point,
            'open_interest': float(self.security_calc_index.open_interest) if isinstance(self.security_calc_index.open_interest, Decimal) else self.security_calc_index.open_interest,
            'delta': float(self.security_calc_index.delta) if isinstance(self.security_calc_index.delta, Decimal) else self.security_calc_index.delta,
            'gamma': float(self.security_calc_index.gamma) if isinstance(self.security_calc_index.gamma, Decimal) else self.security_calc_index.gamma,
            'theta': float(self.security_calc_index.theta) if isinstance(self.security_calc_index.theta, Decimal) else self.security_calc_index.theta,
            'vega': float(self.security_calc_index.vega) if isinstance(self.security_calc_index.vega, Decimal) else self.security_calc_index.vega,
            'rho': float(self.security_calc_index.rho) if isinstance(self.security_calc_index.rho, Decimal) else self.security_calc_index.rho,
        }
    
class SubscriptionModel:
    def __init__(self, subscription):
        self.subscription = subscription
    def to_dict(self):
        return {
            'symbol': self.subscription.symbol,
            'sub_types': [str(types) for types in self.subscription.sub_types],
            'candlesticks': [str(candlesticks) for candlesticks in self.subscription.candlesticks],
        }