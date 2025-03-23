from fastapi import APIRouter, Body
from services.adata_stock import AdataStockService
from schemas.stock_schemas import StockMarketRequest, MarketIndexRequest, MarketMinRequest, ListMarketCurrentRequest
from schemas.response_schemas import AdataPyServiceResponseModel

router = APIRouter(prefix="/stock", tags=["Stock"])


@router.get("/info/all/concept/code/thu", summary="所有A股概念代码信息（同花顺）")
async def get_stock_info_concept_constituent_ths():
    stock_info_all_concept_code_ths = await AdataStockService.get_stock_info_all_concept_code_ths()
    return AdataPyServiceResponseModel(status_code=200, content=stock_info_all_concept_code_ths)


@router.get("/info/all/code", summary="所有A股代码信息")
async def get_stock_info_concept_constituent_ths():
    info_all_code = await AdataStockService.get_info_all_code()
    return AdataPyServiceResponseModel(status_code=200, content=info_all_code)


@router.get("/market", summary="获取单只股票的行情信息-日、周、月 k线")
async def get_stock_market(request: StockMarketRequest = Body(...)):
    stock_market = await AdataStockService.get_stock_market(request.stock_code, request.start_date, request.end_date,
                                                            request.k_type, request.adjust_type)
    return AdataPyServiceResponseModel(status_code=200, content=stock_market)


@router.get("/market/marketindex", summary="获取指数的行情信息-日、周、月 k线")
async def get_market_index(request: MarketIndexRequest = Body(...)):
    market_index = await AdataStockService.get_market_index(request.index_code, request.start_date, request.k_type)
    return AdataPyServiceResponseModel(status_code=200, content=market_index)

@router.get("/market/marketindex/current", summary="获取当前的指数行情-实时")
async def get_market_index(index_code: str):
    market_index_current = await AdataStockService.get_market_index_current(index_code)
    return AdataPyServiceResponseModel(status_code=200, content=market_index_current)


@router.get("/market/marketmin", summary="获取单个股票的今日分时行情")
async def get_market_min(request: MarketMinRequest = Body(...)):
    market_min = await AdataStockService.get_market_min(request.stock_code)
    return AdataPyServiceResponseModel(status_code=200, content=market_min)


@router.get("/market/marketcurrent", summary="获取多个股票最新行情信息")
async def get_market_current(request: ListMarketCurrentRequest = Body(...)):
    market_current = await AdataStockService.list_market_current(request.code_list)
    return AdataPyServiceResponseModel(status_code=200, content=market_current)
