from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)
    API_KEY: str
    
    AUTO_PLAY_GAME: bool = True
    AUTO_TASK: bool = True

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [0, 15]

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
