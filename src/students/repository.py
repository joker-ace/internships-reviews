# -*- coding: utf-8 -*-

from django.contrib.auth.models import User


class Repository(object):

    def user_exists(self, username):
        return User.objects.filter(username=username).exists()
