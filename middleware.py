from fastapi import Request, HTTPException, status
import os
from dotenv import load_dotenv

load_dotenv()
# For simplicity, we load the token from an environment variable
# or a config file. In production, consider using a more secure method.
token = os.getenv("AUTH_TOKEN")

async def auth_middleware(request: Request, call_next):
    # Exclude health check and readiness/liveness routes from authentication
    excluded_paths = ("/health", "/ready", "/live")
    if any(request.url.path.startswith(path) for path in excluded_paths):
        return await call_next(request)
    
    # Check for Authorization header
    authorization = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )

    auth_token = authorization.split(" ")[1]
    # Placeholder for token validation logic
    # In a real application, you would verify the token against your auth system
    if auth_token != token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # If token is valid, proceed with the request
    # You can also log the request or perform additional checks here
    # For example, you might want to log the request path and method
    # logger.info(f"Authenticated request: {request.method} {request.url.path}")
    response = await call_next(request)
    return response
