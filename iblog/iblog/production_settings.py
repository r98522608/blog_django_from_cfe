# import all default settings
from .settings import *

import dj_database_url
DATABASES = {
            'default': dj_database_url.config()
            }

# Static asset configuration
# STATIC_ROOT = 'statics'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")  

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode
DEBUG = False

TEMPLATE_DEBUG = False
