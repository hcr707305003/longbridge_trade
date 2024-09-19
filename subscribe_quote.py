from time import sleep
from longport.openapi import QuoteContext, Config, SubType, PushQuote

class Quote:
    def __init__(self, config):
        self.config = config
    
    def subscribe(self):
        ctx = QuoteContext(self.config)
        ctx.set_on_quote(self.on_quote)
        symbols = ["700.HK", "AAPL.US", "TSLA.US", "NFLX.US"]
        ctx.subscribe(symbols, [SubType.Quote], True)
        sleep(30)

    def on_quote(self, symbol: str, quote: PushQuote):
        print(symbol, quote)