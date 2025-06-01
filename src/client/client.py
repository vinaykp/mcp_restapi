from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
# Get token from environment variable or config file

token = os.getenv("AUTH_TOKEN")

# Create transport with authentication headers
transport = StreamableHttpTransport(
    url="http://127.0.0.1:8000/mcp-server/mcp",
    headers={"Authorization": f"Bearer {token}"}
)
client = Client(transport)

async def main():
    async with client:
        # Get server version
        #version = await client.read_resource("config://version")
        #print(f"Server version: {version}")

        # Get user repositories
        username = "vinaykp"
        #repositories = await client.read_resource(f"repos://{username}")
        repositories = await client.call_tool("list_repositories", {"username": username})
        print(f"Repositories for {username}: {repositories}")

        # List available tools
        #tools = await client.list_tools()
        #print(f"Available tools: {tools}")

        #multiply = await client.call_tool("multiply", {"a": 3.5, "b": 2.0})
        #print(f"Multiply: {multiply}")
      
asyncio.run(main())