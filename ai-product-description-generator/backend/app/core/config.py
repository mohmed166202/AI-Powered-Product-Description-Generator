from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    google_translate_api_key: str
    shopify_api_key: str
    woocommerce_api_key: str
    salla_api_key: str
    zed_api_key: str
    environment: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()