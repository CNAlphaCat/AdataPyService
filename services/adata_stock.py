import adata
import pandas as pd

class AdataStockService:

    @staticmethod
    async def get_stock_info_all_concept_code_ths():
        result = adata.stock.info.all_concept_code_ths()
        return result.astype(str).to_dict(orient='records')

    @staticmethod
    async def get_info_all_code():
        result = adata.stock.info.all_code()
        return result.where(pd.notnull(result), None).to_dict(orient='records')

    @staticmethod
    async def get_stock_market(stock_code: str = '000001', start_date: str = '2025-01-01', end_date: str = None,
                               k_type: int = 1, adjust_type: int = 1):
        result = adata.stock.market.get_market(stock_code, start_date, end_date, k_type, adjust_type)
        return result.astype(str).to_dict(orient='records')

    @staticmethod
    async def get_market_index(index_code: str = '000001', start_date='2020-01-01', k_type: int = 1):
        result = adata.stock.market.get_market_index('399300','2025-01-01')
        print(result)
        result = adata.stock.market.get_market_index('399852', '2025-01-01')
        print(result)
        return result.astype(str).to_dict(orient='records')