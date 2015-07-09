# -*- coding: utf-8 -*-

import os
from ConfigParser import ConfigParser

from common import SOURCES_ROOT

CONFIG_FILE = os.path.join(SOURCES_ROOT, 'config.ini')

config = ConfigParser()
config.read(CONFIG_FILE)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(config.get('database', 'engine')),
        'NAME': config.get('database', 'name'),
        'USER': config.get('database', 'user'),
        'PASSWORD': config.get('database', 'password'),
        'HOST': config.get('database', 'host'),
        'PORT': ''
    }
}
