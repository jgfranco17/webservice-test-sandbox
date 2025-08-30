import logging
import os
from http import HTTPStatus
from time import perf_counter
from typing import Any, Dict

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from backend.core.types import StandardJsonResponse

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sandbox API",
    summary="Mock service for tests",
    description="Provide a simple backend service to run tests against",
    version="0.0.0",
)
startup_time = perf_counter()


@app.get("/", status_code=HTTPStatus.OK, tags=["SYSTEM"])
def root() -> StandardJsonResponse:
    """Project main page."""
    return {"message": "Welcome to the Sandbox API!"}


@app.get("/healthz", status_code=HTTPStatus.OK, tags=["SYSTEM"])
def health_check() -> StandardJsonResponse:
    """Health check for the API."""
    return {
        "status": "healthy",
    }


@app.get("/service-info", status_code=HTTPStatus.OK, tags=["SYSTEM"])
def service_info() -> Dict[str, Any]:
    """Display the Sandbox API project information."""
    return {
        "name": "Sandbox API",
        "description": "Provide a simple backend service to run tests against",
        "uptime_seconds": perf_counter() - startup_time,
    }


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """General exception handler."""
    logger.exception(exc)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": f"Unexpected {exc.status_code} error: {exc.detail}",
            "request_info": {
                "method": request.method,
                "url": request.url.path,
                "headers": request.headers,
            },
        },
    )
