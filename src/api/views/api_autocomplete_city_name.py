# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView


class ApiAutocompleteCityName(CommonBaseView):
    def get(self, request):
        query = request.GET.get('q')
        province = request.GET.get('province')
        cities = self.data.common.find_cities_which_names_start_with(query, province)
        cities = [
            dict(
                name=city.name,
                province=city.province and city.province.name or ''
            ) for city in cities]
        return self.json_response(cities)
