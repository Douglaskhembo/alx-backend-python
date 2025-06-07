from datetime import datetime, time
import logging
from django.http import HttpResponseForbidden


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logging once
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(message)s'
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        path = request.path
        log_message = f"{datetime.now()} - User: {user} - Path: {path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Access allowed only between 6 PM and 9 PM
        self.start_time = time(18, 0, 0)  # 6:00 PM
        self.end_time = time(21, 0, 0)    # 9:00 PM

    def __call__(self, request):
        current_time = datetime.now().time()
        if not (self.start_time <= current_time <= self.end_time):
            return HttpResponseForbidden("Access to the messaging app is restricted outside 6 PM to 9 PM.")
        return self.get_response(request)
