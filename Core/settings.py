import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from pathlib import Path
from dotenv import load_dotenv
import environ

env = environ.Env()
environ.Env.read_env() # Reads the .env file


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = 'django-insecure-i5v#@#3v@=mku9267fq%m39_zp_c6lqeqsq5a4l3=^zb5b%7c@'

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'widget_tweaks',
    'django_bootstrap5',
    # 'crispy_forms',
    'cloudinary',
    'cloudinary_storage',
    'django_daraja',
    'Store',
    'Cart',
    'Account',
    'Payment',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Store.context_processors.categories',
                'Cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'Core.wsgi.application'


# Database

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type

# Crispy templates
CRISPY_TEMPLATE_PACK = 'bootstrap4'
cloudinary.config( 
  cloud_name = os.environ["cloud_name"],
  api_key =  os.environ["api_key"], 
  api_secret = os.environ["api_secret"],
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME':os.environ["CLOUD_NAME"], 
    'API_KEY':os.environ["API_KEY"],
    'API_SECRET':os.environ["API_SECRET"],
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Basket session ID
BASKET_SESSION_ID = 'basket'

# Custom Auth User:
AUTH_USER_MODEL = 'Account.UserBase'
LOGIN_REDIRECT_URL = '/customer/dashboard'
LOGIN_URL = '/customer/login/'

# M-PESA CONFIGURATION:
# ********************************
MPESA_ENVIRONMENT = os.environ['MPESA_ENVIRONMENT']

# Credentials for the daraja app

MPESA_CONSUMER_KEY = os.environ['MPESA_CONSUMER_KEY']
MPESA_CONSUMER_SECRET = os.environ['MPESA_CONSUMER_SECRET']

#Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

MPESA_SHORTCODE = os.environ['MPESA_SHORTCODE']

# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This is only used on sandbox, do not set this variable in production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

MPESA_EXPRESS_SHORTCODE = os.environ['MPESA_EXPRESS_SHORTCODE']

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

MPESA_SHORTCODE_TYPE = os.environ['MPESA_SHORTCODE_TYPE']

# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY = os.environ['MPESA_PASSKEY']

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = os.environ['MPESA_INITIATOR_USERNAME']

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_SECURITY_CREDENTIAL = os.environ['MPESA_INITIATOR_SECURITY_CREDENTIAL']

# **********************************8

# Pass reset
PASSWORD_RESET_TIMEOUT_DAYS = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Bottom of settings.py 
# Twilio SendGrid

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey' # Name for all the SenGrid accounts
EMAIL_HOST_PASSWORD = env('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = env('FROM_EMAIL') # The email you'll be sending emails from
# Server	= 'smtp.sendgrid.net'
# Ports =25, 587
# Username='apikey'
# Password= env('SENDGRID_API_KEY')

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

