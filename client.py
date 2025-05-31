from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
import asyncio


# Create transport with authentication headers
transport = StreamableHttpTransport(
    url="http://127.0.0.1:4200/mcp-server/mcp",
    # headers={"Authorization": "Bearer your-token-here"}
)
client = Client(transport)

async def main():
    async with client:
        # Get server version
        version = await client.read_resource("config://version")
        print(f"Server version: {version}")
        # Get user profile
        profile = await client.read_resource("users://123/profile")
        print(f"User profile: {profile}")

        # List available tools
        tools = await client.list_tools()
        # print(f"Available tools: {tools}")
        greeting = await client.call_tool("greet", {"name": "Alice......"})
        print(f"Greeting: {greeting}")
        multiply = await client.call_tool("multiply", {"a": 3.5, "b": 2.0})
        print(f"Multiply: {multiply}")
      
asyncio.run(main())