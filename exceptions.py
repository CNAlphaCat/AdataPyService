from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse


async def http_exception_handler(request: Request, exc: Exception):
    if not isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )