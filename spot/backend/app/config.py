from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:ZbulPNsrTWXFSwTecbEaBLLMpUmzmomm@junction.proxy.rlwy.net:13322/railway"
    PROJECT_NAME: str = "spot"


@lru_cache()
def get_settings():
    return Settings()
