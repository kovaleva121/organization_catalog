from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Organization Catalog API'
    VERSION: str = '1.0.0'
    API_V1_STR: str = '/api/v1'

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def DATABASE_URL(self) -> str:
        return f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}'

    API_KEY: str
    API_KEY_NAME: str = 'X-API-Key'

    class Config:
        env_file = '.env'


settings = Settings()
