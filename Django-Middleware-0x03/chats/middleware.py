from datetime import datetime, time, timedelta
from collections import defaultdict, deque
import logging
from django.http import HttpResponseForbidden

# Middleware 1: Logs each user request
class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
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


# Middleware 2: Restricts access by time (between 6 PM and 9 PM only)
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.start_time = time(18, 0, 0)  # 6 PM
        self.end_time = time(21, 0, 0)    # 9 PM

    def __call__(self, request):
        current_time = datetime.now().time()
        if not (self.start_time <= current_time <= self.end_time):
            return HttpResponseForbidden("Access to the messaging app is restricted outside 6 PM to 9 PM.")
        return self.get_response(request)


# Middleware 3: Limit POST requests to 5 per minute per IP
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_per_ip = defaultdict(deque)
        self.limit = 5  # messages
        self.time_window = timedelta(minutes=1)

    def __call__(self, request):
        if request.method == 'POST':
            ip = self.get_ip_address(request)
            now = datetime.now()
            request_times = self.requests_per_ip[ip]

            # Remove timestamps older than the time window
            while request_times and now - request_times[0] > self.time_window:
                request_times.popleft()

            if len(request_times) >= self.limit:
                return HttpResponseForbidden("Rate limit exceeded: Max 5 messages per minute.")

            request_times.append(now)

        return self.get_response(request)

    def get_ip_address(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')
