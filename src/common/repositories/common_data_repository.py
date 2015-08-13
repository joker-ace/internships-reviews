# -*- coding: utf-8 -*-
from common.models.university import University
from common.models.faculty import Faculty
from common.models.province import Province
from common.models.city import City


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

    def get_province_by_id(self, province):
        try:
            return Province.objects.get(pk=province)
        except Province.DoesNotExist:
            return None

    def get_cities_list(self):
        return City.objects.all()

    def find_faculties_which_names_starts_with(self, query):
        return Faculty.objects.filter(name__istartswith=query)

    def find_cities_which_names_start_with(self, query, province=None):
        cities = self.get_cities_list().filter(name__istartswith=query)
        if province:
            cities = cities.filter(province=province)
        return cities

    def get_city_by_name(self, name):
        try:
            return City.objects.get(name=name)
        except City.DoesNotExist:
            return None

    def add_city(self, city_name, city_province, return_new_instance=False):
        city = City()
        city.name = city_name
        city.province = city_province
        city.save()
        return city