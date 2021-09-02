from time import time

import re

from .models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        before_time = time()
        response = self.get_response(request)
        after_time = time()
        execution_time = before_time - after_time
        if re.search('admin', request.path):
            Logger.objects.create(path=request.path, method=request.method, execution_time=execution_time)

        return response
