from typing import Optional
from pydantic import BaseModel

class StockMarketRequest(BaseModel):
    stock_code: str
    start_date: Optional[str] = '2025-01-01'
    end_date: Optional[str] = None
    k_type:Optional[int] = 1
    adjust_type:Optional[int] = 1