# -*- coding: utf-8 -*-
from common.models.university import University
from common.models.faculty import Faculty
from common.models.province import Province


class CommonDataRepository(object):
    def get_university_by_pk(self, university):
        try:
            return University.objects.get(pk=university)
        except (University.DoesNotExist, ValueError):
            return None

    def get_faculty_by_pk(self, faculty):
        try:
            return Faculty.objects.get(pk=faculty)
        except (Faculty.DoesNotExist, ValueError):
            return None

    def get_universities_list(self):
        return University.objects.all()

    def get_university_faculties_list(self, university):
        return Faculty.objects.filter(university=university)

    def get_provinces_list(self):
        return Province.objects.all()