import os

class Config:
    APP_NAME = "Secure DevOps Backend"
    API_TOKEN = os.getenv("API_TOKEN", "dev-token")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
