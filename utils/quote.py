from longport.openapi import QuoteContext, Period, Market, SecurityListCategory, AdjustType, CalcIndex, SubType, PushQuote
from datetime import datetime
from time import sleep
from utils.model import (
    SecurityModel,
    SecurityStaticInfoModel,
    SecurityQuoteModel,
    TradeModel,
    CandlestickModel,
    CapitalFlowLineModel,
    CapitalDistributionResponseModel,
    SecurityCalcIndexModel,
    SubscriptionModel
)
from utils.tools import *

class Quote:
    def __init__(self, config):
        self.config = config
        self.quote_ctx = QuoteContext(self.config)

    async def security_list(self):
        """
        获取标的列表
        param: market: 市场，目前只支持 US
        param: category: 市场下分类，目前只支持 Overnight
        """
        return [SecurityModel(security).to_dict() for security in self.quote_ctx.security_list(
            Market.US, 
            SecurityListCategory.Overnight
        )]
        
        
    async def security_static_info(self, symbol):
        """
        获取标的基础信息
        param: security: 标的代码，如 AAPL
        """
        if isinstance(symbol, str):
            # 按逗号切割并去除空字符串
            symbol_list = [item.strip() for item in symbol.split(',') if item.strip()]
        elif isinstance(symbol, list):
            symbol_list = symbol
        else:
            symbol_list = []

        static_info = []
        if isinstance(symbol_list, list) and len(symbol_list) > 0:
            static_info = self.quote_ctx.static_info(symbol_list)

        return [SecurityStaticInfoModel(info).to_dict() for info in static_info]
        
    async def security_quote_info(self, symbol):
        """
        获取标的实时行情
        param: symbol: 标的代码，如 AAPL
        """
        if isinstance(symbol, str):
            # 按逗号切割并去除空字符串
            symbol_list = [item.strip() for item in symbol.split(',') if item.strip()]
        elif isinstance(symbol, list):
            symbol_list = symbol
        else:
            symbol_list = []

        quote_info = []
        if isinstance(symbol_list, list) and len(symbol_list) > 0:
            quote_info = self.quote_ctx.quote(symbol_list)

        return [SecurityQuoteModel(info).to_dict() for info in quote_info]
    
    async def security_trades(self, symbol, limit = 1000):
        """
        获取标的成交明细
        param: symbol: 标的代码，使用 ticker.region 格式，例如：700.HK
        param: limit: 请求数量最大为 1000
        """
        return [TradeModel(trades).to_dict() for trades in self.quote_ctx.trades(symbol, int(limit))]
    
    async def security_history_candlesticks(self, symbol, limit = 1000, date = None):
        """
        获取标的历史K线数据
        param: symbol: 标的代码，使用 ticker.region 格式，例如：700.HK
        param: limit: 请求数量最大为 1000
        param: date: 日期，默认为 2021-01-01
        """
        if date is None:
            date = datetime(datetime.now().year, 1, 1)
    
        return [CandlestickModel(trades).to_dict() for trades in self.quote_ctx.history_candlesticks_by_offset(symbol, Period.Day, AdjustType.NoAdjust, True, date, int(limit))]
    
    async def security_capital_flow(self, symbol):
        """
        获取标的当日资金流向
        param: symbol: 标的代码，使用 ticker.region 格式，例如：700.HK
        """
        return [CapitalFlowLineModel(trades).to_dict() for trades in self.quote_ctx.capital_flow(symbol)]
    
    async def security_capital_distribution(self, symbol):
        """
        获取标的当日资金分布
        param: symbol: 标的代码，使用 ticker.region 格式，例如：700.HK
        """
        return CapitalDistributionResponseModel(self.quote_ctx.capital_distribution(symbol)).to_dict()
        
    async def security_calc_indexes(self, symbol):
        """
        获取标的计算指标
        param: symbol: 标的代码，使用 ticker.region 格式，例如：700.HK
        """
        if isinstance(symbol, str):
            # 按逗号切割并去除空字符串
            symbol_list = [item.strip() for item in symbol.split(',') if item.strip()]
        elif isinstance(symbol, list):
            symbol_list = symbol
        else:
            symbol_list = []
        return [SecurityCalcIndexModel(trades).to_dict() for trades in self.quote_ctx.calc_indexes(symbol_list, [CalcIndex.LastDone,CalcIndex.ChangeValue,CalcIndex.ChangeRate,CalcIndex.Volume,CalcIndex.Turnover,CalcIndex.YtdChangeRate,CalcIndex.TurnoverRate,CalcIndex.TotalMarketValue,CalcIndex.CapitalFlow,CalcIndex.Amplitude,CalcIndex.VolumeRatio,CalcIndex.PeTtmRatio,CalcIndex.PbRatio,CalcIndex.DividendRatioTtm,CalcIndex.FiveDayChangeRate,CalcIndex.TenDayChangeRate,CalcIndex.HalfYearChangeRate,CalcIndex.FiveMinutesChangeRate,CalcIndex.ExpiryDate,CalcIndex.StrikePrice,CalcIndex.UpperStrikePrice,CalcIndex.LowerStrikePrice,CalcIndex.OutstandingQty,CalcIndex.OutstandingRatio,CalcIndex.Premium,CalcIndex.ItmOtm,CalcIndex.ImpliedVolatility,CalcIndex.WarrantDelta,CalcIndex.CallPrice,CalcIndex.ToCallPrice,CalcIndex.EffectiveLeverage,CalcIndex.LeverageRatio,CalcIndex.ConversionRatio,CalcIndex.BalancePoint,CalcIndex.OpenInterest,CalcIndex.Delta,CalcIndex.Gamma,CalcIndex.Theta,CalcIndex.Vega,CalcIndex.Rho])]

    async def security_candlesticks(self, symbol, period = "day", limit = 1000):
        if period.isalpha():
            if period == "day":
                period_raw = Period.Day
            elif period == "week":
                period_raw = Period.Week
            elif period == "month":
                period_raw = Period.Month
            elif period == "year":
                period_raw = Period.Year
            else:
                period_raw = Period.Day
        elif period.isdigit():
            period = int(period)
            if period == 1:
                period_raw = Period.Min_1
            elif period == 5:
                period_raw = Period.Min_5
            elif period == 15:
                period_raw = Period.Min_15
            elif period == 30:
                period_raw = Period.Min_30
            elif period == 60:
                period_raw = Period.Min_60
            else:
                period_raw = Period.Min_1
        else:
            period_raw = Period.Day

        return [CandlestickModel(trades).to_dict() for trades in self.quote_ctx.candlesticks(symbol, period_raw, int(limit), AdjustType.NoAdjust)]
    
    async def security_subscribe(self, symbol, type = "subscribe", sub_type = None):
        """
        订阅|取消订阅 => 行情数据|订阅标的
        """
        if isinstance(symbol, str):
            # 按逗号切割并去除空字符串
            symbol_list = [item.strip() for item in symbol.split(',') if item.strip()]
        elif isinstance(symbol, list):
            symbol_list = symbol
        else:
            symbol_list = []
        
        if (sub_type is None) or (sub_type.strip() == ""):
            sub_type_list = [SubType.Quote, SubType.Depth, SubType.Brokers, SubType.Trade]
        elif isinstance(sub_type, str):
            sub_type_list = []
            sub_type_arr = [item.strip() for item in sub_type.split(',') if item.strip()]
            if 'quote' in sub_type_arr:
                sub_type_list.append(SubType.Quote)
            if 'depth' in sub_type_arr:
                sub_type_list.append(SubType.Depth)
            if 'brokers' in sub_type_arr:
                sub_type_list.append(SubType.Brokers)
            if 'trade' in sub_type_arr:
                sub_type_list.append(SubType.Trade)

        type = type.strip()
        if (type == "subscribe") or (type == ''):
            # 订阅行情数据
            self.quote_ctx.subscribe(symbol_list, sub_type_list, is_first_push=True)
        elif type == "unsubscribe":
            # 取消订阅行情数据
            self.quote_ctx.unsubscribe(symbol_list, sub_type_list)

        return [SubscriptionModel(subscriptions).to_dict() for subscriptions in self.quote_ctx.subscriptions()]