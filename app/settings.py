import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    server_host: str = os.environ.get('SERVER_HOST')
    server_port: int = os.environ.get('SERVER_PORT')
    access_token: str = os.environ.get('ACCESS_TOKEN')
    
settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)