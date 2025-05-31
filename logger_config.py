import sys
from loguru import logger
from pathlib import Path

# Create logs directory if it doesn't exist
log_path = Path("logs")
log_path.mkdir(exist_ok=True)

# Remove default logger
logger.remove()

# Add console logger with color
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

# Add file logger with rotation
logger.add(
    "logs/mcp_server.log",
    rotation="500 MB",
    retention="10 days",
    compression="zip",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    backtrace=True,
    diagnose=True
)

# Configure exception catching
logger.add(
    "logs/error.log",
    rotation="100 MB",
    retention="5 days",
    compression="zip",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="ERROR",
    backtrace=True,
    diagnose=True
)
