from pathlib import Path
from . import get_secret
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = get_secret("SECRET_KEY")

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": (
        {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "db",
            "PORT": "5432",
        }
    )
}


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
