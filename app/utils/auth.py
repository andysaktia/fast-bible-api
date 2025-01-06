from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader

API_KEY = "your-secret-token"
api_key_header = APIKeyHeader(name="Authorization", auto_error=True)

def validate_token(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API token")
    return api_key
