from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from gateway.config import MCP_GATEWAY_TOKEN

security = HTTPBearer()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    if token != MCP_GATEWAY_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return True