from pathlib import Path
from environs import Env

# Initialize environs
env = Env()
env.read_env()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = env.str("DJANGO_SECRET")
DEBUG = env.bool("DJANGO_DEBUG", default=True)
# ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost"])
ALLOWED_HOSTS = ["*"]


# Installed apps
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "rest_framework",
    "payments.apps.PaymentsConfig",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

# Root URL configuration
ROOT_URLCONF = "core.urls"

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB", default="app_database"),
        "USER": env.str("POSTGRES_USER", default="postgres"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default="password"),
        "HOST": env.str("POSTGRES_HOST", default="localhost"),
        "PORT": env.int("POSTGRES_PORT", default=5432),
        "OPTIONS": {"options": "-c search_path=users_api"},
    }
}

# Static files
STATIC_URL = "static/"

# Stripe settings
if DEBUG:
    STRIPE_PUBLIC_KEY = config("TEST_STRIPE_PUBLIC_KEY")
    STRIPE_SECRET_KEY = config("TEST_STRIPE_SECRET_KEY")
else:
    STRIPE_PUBLIC_KEY = config("LIVE_STRIPE_PUBLIC_KEY")
    STRIPE_SECRET_KEY = config("LIVE_STRIPE_SECRET_KEY")


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

KAFKA_TOPIC = env.str("KAFKA_TOPIC", default="default_topic")
KAFKA_SERVERS = env.list("KAFKA_SERVERS", default=["kafka:9092"])