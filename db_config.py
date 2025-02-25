import os

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "gis")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "docker")
    DB_PORT = os.getenv("DB_PORT", "25432")
    DB_USER = os.getenv("DB_USER", "docker")