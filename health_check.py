import datetime
import asyncio
from typing import Dict, Any
from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

health_router = APIRouter()

async def check_external_api_availability():
    """Simulates checking an external API."""
    await asyncio.sleep(0.02) # Simulate network latency
    return True

@health_router.get("/health", response_model=Dict[str, Any], status_code=status.HTTP_200_OK, tags=["Health"])
async def health_check(request: Request):
    """
    Performs a comprehensive health check of the MCP server and its dependencies.
    """
    health_status = {
        "status": "UP",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "service": "FastMCP Server",
        "dependencies": {}
    }

    # Perform dependency checks
    api_ok = await check_external_api_availability()

    health_status["dependencies"]["external_api"] = "UP" if api_ok else "DOWN"

    # Determine overall status
    if not ( api_ok):
        health_status["status"] = "DEGRADED"
    return health_status

@health_router.get("/ready", status_code=status.HTTP_200_OK, tags=["Health"])
async def readiness_check():
    """
    Checks if the server is ready to accept traffic.
    This might be stricter than a liveness check, potentially failing if
    critical dependencies are not fully initialized or connected.
    """
    api_ok = await check_external_api_availability()

    if not (api_ok):
        # If critical dependencies are down, the server is not ready to serve requests.
        return JSONResponse(
            content={"status": "NOT_READY", "reason": "Critical dependencies unavailable"},
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )
    return {"status": "READY"}


@health_router.get("/live", status_code=status.HTTP_200_OK, tags=["Health"])
async def liveness_check():
    """
    Checks if the server is alive.
    This is a basic check to ensure the server process is running.
    """
    return {"status": "ALIVE"}


