from fastmcp import FastMCP

# You can also add instructions for how to interact with the server
mcp = FastMCP(
    name="HelpfulAssistant",
    mask_error_details=True,  # Mask error details for security
    instructions="""
        This server provides data analysis tools.
        You can ask for help with data processing, analysis, and visualization.
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

# Run the server
if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=4200,
        path="/mcp1",
        log_level="debug",
    ) 
# To run this server, python server.py