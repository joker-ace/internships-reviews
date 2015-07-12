# -*- coding: utf-8 -*-
from common.models.university import University
from common.models.faculty import Faculty


class Repository(object):
    def get_university(self, university):

        try:
            university = int(university)
        except ValueError:
            return None

        try:
            return University.objects.get(pk=university)
        except University.DoesNotExist:
            return None

    def get_faculty(self, faculty):

        try:
            faculty = int(faculty)
        except ValueError:
            return None

        try:
            return Faculty.objects.get(pk=faculty)
        except Faculty.DoesNotExist:
            return None

    def get_universities_list(self):
        return University.objects.all()

    def get_university_faculties_list(self, university=None):
        return Faculty.objects.filter(university=university)
