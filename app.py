from fastapi import FastAPI, HTTPException
from routers.adata_stock_router import router as stock_router
from exceptions import http_exception_handler

app = FastAPI()
app.include_router(stock_router)
app.add_exception_handler(HTTPException, http_exception_handler)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)