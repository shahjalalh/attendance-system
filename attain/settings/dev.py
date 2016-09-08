from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=hu*b&izugv5r_$4r5o)wkp_rp^1&(hiy@0#743q$m0vv6!dit'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
