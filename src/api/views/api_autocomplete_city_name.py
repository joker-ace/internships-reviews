# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView

# This handler for processing autocomplete for city name

class ApiAutocompleteCityName(CommonBaseView):
    def get(self, request):
        # get search values from url parameters
        query = request.GET.get('q')
        province = request.GET.get('province')

        # get cities with provided parameters
        cities = self.data.common.find_cities_which_names_start_with(query, province)

        # create list of objects
        cities = [
            dict(
                name=city.name,
                province=city.province and city.province.name or ''
            ) for city in cities]

        # return list as json
        return self.json_response(cities)
