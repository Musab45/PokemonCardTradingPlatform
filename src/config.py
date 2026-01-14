from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    
    # app
    app_name: str = 'Pokemon Card Trading Platform'
    app_version: str = '1.0.0'
    debug: bool = False
    
    # database
    database_url: str
    database_echo: bool = False
    
    # security
    secret_key: str
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    
    # CORS
    allowed_origin: list[str] = ['http://localhost:3000']
    
    # rate limiting
    rate_limiting_per_minute: int = 60
    
    # pagination
    default_page_size: int = 20
    max_page_size: int =100
    
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False
    )

# get cached setting instance
@lru_cache
def get_settings() -> Settings:
    return Settings()