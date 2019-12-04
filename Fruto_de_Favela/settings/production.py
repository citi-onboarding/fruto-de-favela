from .base import *


DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = os.environ.get('DROPBOX_OAUTH2_TOKEN')
DROPBOX_ROOT_PATH = '/media/'

import django_heroku
django_heroku.settings(locals())