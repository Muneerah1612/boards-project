from decouple import config

ENVIRONMENT = config('ENVIRONMENT')
if ENVIRONMENT == 'development':
    from .development import * # noqa

elif ENVIRONMENT == 'testing':
    from .testing import *  # noqa

elif ENVIRONMENT == 'production':
    from .production import *  # noqa