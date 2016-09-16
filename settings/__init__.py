# -*- coding: utf-8 -*-

try:
    from .local import *
except ImportError:
    print("There is no local settings, create settings/local.py")
