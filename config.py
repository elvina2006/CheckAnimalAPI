import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGODB_URL = os.getenv('MONGODB_URL')
    ROBOFLOW_URL = os.getenv('ROBOFLOW_URL')
    DB_NAME = os.getenv('DB_NAME')


config = Config()
