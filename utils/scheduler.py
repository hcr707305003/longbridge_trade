from longport.openapi import QuoteContext, Config, Market, SecurityListCategory
from utils.model import (
    SecurityModel
)
from utils.sqliteDB import SqliteHandle
from utils.tools import *
import asyncio

class Scheduler:
    def __init__(self, long_bridge_config):
        self.long_bridge_config = long_bridge_config
        self.quote_ctx = QuoteContext(self.long_bridge_config)
        self.db = SqliteHandle("longbridge.db")
        
    def run(self):
        # 同步标的
        asyncio.run(self.syncSecurity())
    
    async def syncSecurity(self):
        security_list = [SecurityModel(security).to_dict() for security in self.quote_ctx.security_list(
            Market.US, 
            SecurityListCategory.Overnight
        )]
        async def execute_db():
            for security in security_list:
                await self.db.save_data("security", security, {"symbol": security["symbol"]})
                
        await db_handle(self.db, execute_db)