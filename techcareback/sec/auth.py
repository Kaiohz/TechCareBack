from fastapi import HTTPException,Security
from techcareback.util.config import Config
from fastapi.security.api_key import APIKeyHeader
from techcareback.util.strings import AUTH_ERROR

api_key_header = APIKeyHeader(name="api_key", auto_error=False)

Config = Config()

async def get_api_key(api_key_header: str= Security(api_key_header)):
    if api_key_header != Config.AUTH_KEY:
        raise HTTPException(status_code=401, detail=AUTH_ERROR)