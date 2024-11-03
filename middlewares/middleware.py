from datetime import datetime
from django.utils.deprecation import MiddlewareMixin


class CustomMiddleware(MiddlewareMixin):
    """
    Processes the request. updates the last_active_datetime of
    the authenticated user and sets the session expiry to 1 minute.
    """
    def process_request(self, request):
        request.time = datetime.now()
        user = request.user
        if not user.is_anonymous:
            user.last_active_datetime = request.time
            user.save()
            request.session.set_expiry(60)