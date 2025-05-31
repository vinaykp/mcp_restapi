from fastmcp import FastMCP

# Initialize MCP
mcp = FastMCP(
    name="GeneralMCPServer",
    mask_error_details=True,  # Mask error details for security
    instructions="""
        Welcome to the General MCP Server! This server provides basic resources and tools.
        """,
    tags={"data", "analysis", "visualization"},
)

# Static resource
@mcp.resource("config://version")
async def get_version(): 
    return "0.0.1"

# Dynamic resource template
@mcp.resource("users://{user_id}/profile")
async def get_profile(user_id: int):
    # Fetch profile for user_id...
    return {"name": f"User {user_id}", "status": "active"}

# Tools
@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

@mcp.tool()
async def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"
