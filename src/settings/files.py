# -*- coding: utf-8 -*-

import os

from common import SOURCES_ROOT, BASE_DIR

STATICFILES_DIRS = (
    os.path.join(SOURCES_ROOT, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static_content')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_content')
