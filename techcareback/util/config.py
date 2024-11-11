from pydantic import Field
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    AUTH_KEY: str = Field(..., json_schema_extra={'env': 'AUTH_KEY'})
    ALLOWED_ORIGINS: list[str] = Field(..., json_schema_extra={'env': 'ALLOWED_ORIGINS'})