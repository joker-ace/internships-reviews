# -*- coding: utf-8 -*-

from common.models.error_log import ErrorLog
from django.utils.decorators import method_decorator
import traceback


def exception_logging(View):
    def exception_logger(dispatch_function):
        def wrapper(request, *args, **kwargs):
            try:
                return dispatch_function(request, *args, **kwargs)
            except Exception as e:
                error_log = ErrorLog()
                error_log.stacktrace = traceback.format_exc()
                error_log.message = e.message
                error_log.error_url = request.path_info
                error_log.save()
                raise e

        return wrapper

    View.dispatch = method_decorator(exception_logger)(View.dispatch)
    return View
