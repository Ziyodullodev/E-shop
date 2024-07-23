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
DB_USER_NM = get_secret("DB_USER_NM")
DB_USER_PW = get_secret("DB_USER_PW")
DB_IP = get_secret("DB_IP")
DB_PORT = get_secret("DB_PORT")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER_NM,
        "PASSWORD": DB_USER_PW,
        "HOST": DB_IP,
        "PORT": DB_PORT,
    }
}


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
