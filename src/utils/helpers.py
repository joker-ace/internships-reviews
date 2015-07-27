# -*- coding: utf-8 -*-

def is_int(value):
    try:
        int(value)
        return True
    except:
        return False
