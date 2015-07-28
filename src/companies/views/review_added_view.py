# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import resolve_url

from common.views.common_base_view import CommonBaseView


class ReviewAddedView(CommonBaseView):

    template_name = 'companies/review_add_message.html'

    @method_decorator(login_required)
    def get(self, request):
        messages_list = messages.get_messages(request)
        message = filter(lambda m: m.level_tag == 'success', messages_list)
        if not message:
            return self.redirect_to(view_name='companies_list_page')

        self.update_context({
            'redirect_url': resolve_url('companies_list_page'),
            'message': message.pop()
        })
        return self.response()