import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_HOST = "0.0.0.0"
    API_PORT = 8000
    DEBUG = os.getenv("DEBUG", "False") == "True"
    FIREBASE_KEY = os.getenv("FIREBASE_KEY", "")
    DATABASE_URL = os.getenv("DATABASE_URL", "localhost")
    EMOTION_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
    CRISIS_KEYWORDS = [
        "kill myself", "suicide", "harm myself",
        "hurt myself", "end it all", "don't want to live"
    ]
    MAX_MEMORY_ITEMS = 1000
    MEMORY_RETENTION_DAYS = 365
    FOUR_NOBLE_TRUTHS = {
        "dukkha": "suffering exists",
        "samudaya": "suffering has causes",
        "nirodha": "suffering can end",
        "magga": "path to end suffering"
    }

config = Config()
