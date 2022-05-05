from django.contrib.messages import constants as message_constants
from pathlib import Path,os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o-ixn@m$#m))8^vxu&2b@nv5$c(a+kou*0-&gz%++3txj=3+ve'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'myapp',
    'widget_tweaks',
    'social_django',# <-- Here
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',# <-- Here
]

ROOT_URLCONF = 'trip.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'trip.wsgi.application'



AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',    # <-- Here
    'social_core.backends.instagram.InstagramOAuth2',  # <-- Here
    'social_core.backends.google.GoogleOAuth2',        # <-- Here
    'social_core.backends.twitter.TwitterOAuth',       # <-- Here
    'social_core.backends.github.GithubOAuth2',        # <-- Here

    'django.contrib.auth.backends.ModelBackend',       # <-- Here
)






SOCIAL_AUTH_FACEBOOK_KEY = '214820970184927'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'dbabdff44b2ad9c5d57422da3556d2f4'  # App Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '976490283837-jlc6kll7ltsqhnq99cbaomftttv96vb7.apps.googleusercontent.com'  # App ID
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'A-G9r0a38pwkFQiyWFw2-SMm'  # App Secret
SOCIAL_AUTH_INSTAGRAM_KEY = '1000320030494985'  # App ID
SOCIAL_AUTH_INSTAGRAM_SECRET = '3f0390f498b3ec6f3218ea23b6c21888'  # App Secret
LOGIN_REDIRECT_URL = '/dashboard'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','mysite.org']  # <-- Here






# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR/'static'
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'

MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger', }


# Key id - rzp_test_TogcIcgTx8aTuq
# Key Secret - kROXDyYlNtDqqgzihyr44cLM