from pathlib import Path
import os
from . import get_secret

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]


DB_NAME = get_secret("DB_NAME")
DB_USERNAME = get_secret("DB_USERNAME")
DB_PASSWORD = get_secret("DB_PASSWORD")
DB_HOSTNAME = get_secret("DB_HOSTNAME")
DB_PORT = get_secret("DB_PORT")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USERNAME,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOSTNAME,
        "PORT": DB_PORT,
    }
}


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
