import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from tools.mcp_server import mcp
from health_check import health_router
from loguru import logger
import config.logger_config as logger_config  # This will setup the logger configuration
from middleware.middleware import auth_middleware

logger.info("Initializing MCP HTTP Server")

# Create the ASGI app
mcp_app = mcp.http_app(path='/mcp')

# Create a FastAPI app and mount the MCP server
app = FastAPI(lifespan=mcp_app.lifespan,
                  version="0.0.1",
                  title="HTTP Server")

logger.debug("Configuring CORS middleware")
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)  

# Add the middleware to the app
app.middleware("http")(auth_middleware)

app.mount("/mcp-server", mcp_app)
# The MCP endpoint will be available at /mcp-server/mcp of the resulting FastAPI app.

# Run the server
if __name__ == "__main__":
    logger.info(f"Server starting on http://127.0.0.1:8000")
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="debug"
    )
