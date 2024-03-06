import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SERVER_NAME = "localhost:7001"
    DEBUG = True

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"
