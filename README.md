# MCP REST API

## Overview
This project implements a REST API server for the Model Context Protocol (MCP). It provides endpoints for managing and interacting with MCP resources.

## Project Structure
- `client.py`: Handles client-side interactions.
- `health_check.py`: Implements health check endpoints for the server.
- `logger_config.py`: Configures logging for the application.
- `mcp_server.py`: Core server logic for the MCP REST API.
- `middleware.py`: Middleware components for request/response processing.
- `server.py`: Entry point for starting the server.
- `pyproject.toml`: Project configuration and dependencies.
- `logs/`: Directory containing log files (`error.log`, `mcp_server.log`).

## Requirements
- Python 3.12 or higher
- Dependencies listed in `pyproject.toml`

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp_restapi
   ```
2. Install dependencies:
   ```bash
   pip install -e .
   ```

## Running the Server
Start the server using the following command:
```bash
python server.py
```

## Logging
Log files are stored in the `logs/` directory. The following logs are available:
- `error.log`: Records error messages.
- `mcp_server.log`: General server logs.

## Health Check
The health check endpoint can be accessed to verify the server's status. Refer to `health_check.py` for implementation details.

## License
This project is licensed under the MIT License. See the LICENSE file for details.