from typing import Optional, List
from pydantic import BaseModel

class StockMarketRequest(BaseModel):
    stock_code: str
    start_date: Optional[str] = '2025-01-01'
    end_date: Optional[str] = None
    k_type:Optional[int] = 1
    adjust_type:Optional[int] = 1

class MarketIndexRequest(BaseModel):
    index_code: str
    start_date: Optional[str] = '2025-01-01'
    k_type:Optional[int] = 1

class MarketMinRequest(BaseModel):
    stock_code: str

class ListMarketCurrentRequest(BaseModel):
    code_list:Optional[List[str]] = None