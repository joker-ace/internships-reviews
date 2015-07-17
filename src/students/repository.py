# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from students.models.student import Student


class Repository(object):
    def user_exists(self, username):
        return User.objects.filter(username=username).exists()

    def create_user(self, model_form):
        user = model_form.save(commit=False)
        user.username = user.email
        user.set_password(user.password)
        user.save()

    def university_record_exists(self, user):
        return Student.objects.filter(user=user).exists()