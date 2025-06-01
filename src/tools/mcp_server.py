from fastmcp import FastMCP
import httpx
from fastmcp.server.dependencies import get_http_headers
from loguru import logger

# Initialize MCP
mcp = FastMCP(
    name="GeneralMCPServer",
    mask_error_details=True,  # Mask error details for security
    instructions="""
        You are a general-purpose MCP server that provides various tools and resources.
        """,
    tags={"data", "analysis"},
)

# Static resource
@mcp.resource("config://version")
async def get_version(): 
    return "0.0.1"

@mcp.resource("repos://{username}")
async def get_user_repositories(username: str):
    # call the tool to list repositories for the given username
    logger.debug(f"Fetching repositories for user: {username}")
    return await list_repositories(username)

@mcp.tool()
async def list_repositories(username: str) -> dict:
    """List repositories of the given username."""
    headers = get_http_headers()
    logger.debug(f"Fetching repositories for user: {username} with headers: {headers}")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}/repos", headers=headers)
        logger.debug(f"Response status code: {response.status_code} for user: {username}")
        if response.status_code != 200:
            return {"error": f"Failed to fetch repositories for user {username}"}

        repos = response.json()
        return {
            "username": username,
            "repositories": [
                {"name": repo["name"], "description": repo.get("description", "No description")} for repo in repos
            ]
        }

@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b
