from pydantic_settings import BaseSettings

class BaseSettingWrapper(BaseSettings):

    class Config:
        env_file=".env"
        extra="allow"