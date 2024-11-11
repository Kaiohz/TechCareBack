from fastapi import HTTPException,Security
from techcareback.util.config import Config
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="api_key", auto_error=False)

Config = Config()

async def get_api_key(api_key_header: str= Security(api_key_header)):
    """
    Validates the provided API key.

    Args:
        api_key (str): The API key to be validated.

    Raises:
        HTTPException: If the API key is invalid or unauthorized.

    Returns:
        None
    """
    if api_key_header != Config.AUTH_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key or Unauthorized Access")