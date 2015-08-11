# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from common.views.common_base_view import CommonBaseView


class LogoutView(CommonBaseView):
    def get(self, request):
        logout(request)
        return self.redirect_to('login_page')
