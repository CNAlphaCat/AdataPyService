from fastapi import APIRouter, Body
from services.adata_stock import AdataStockService
from schemas.stock_schemas import StockMarketRequest

router = APIRouter(prefix="/stock", tags=["Stock"])


@router.get("/info/all/concept/code/thu", summary="所有A股概念代码信息（同花顺）")
async def get_stock_info_concept_constituent_ths():
    stock_info_all_concept_code_ths = await AdataStockService.get_stock_info_all_concept_code_ths()
    return {
        "status": 200,
        "data": stock_info_all_concept_code_ths
    }

@router.get("/info/all/code", summary="所有A股代码信息")
async def get_stock_info_concept_constituent_ths():
    info_all_code = await AdataStockService.get_info_all_code()
    return {
        "status": 200,
        "data": info_all_code
    }

@router.get("/market", summary="获取单只股票的行情信息-日、周、月 k线")
async def get_stock_market(request: StockMarketRequest = Body(...)):
    stock_market = await AdataStockService.get_stock_market(request.stock_code, request.start_date, request.end_date,
                                                       request.k_type, request.adjust_type)
    return {
        "status": 200,
        "data": stock_market
    }

@router.get("/market/marketindex", summary="获取指数的行情信息-日、周、月 k线")
async def get_market_index():
    market_index = await AdataStockService.get_market_index()
    return {
        "status": 200,
        "data": market_index
    }