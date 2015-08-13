# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView

# This handler for processing autocomplete for faculty name

class ApiAutocompleteFacultyName(CommonBaseView):
    def get(self, request):
        # get search values from url parameters
        query = request.GET.get('q')
        # get cities with provided parameters
        faculties = self.data.common.find_faculties_which_names_starts_with(query)
        # create list of objects
        faculties = [faculty.to_dict() for faculty in faculties]
        # return list as json
        return self.json_response(faculties)
