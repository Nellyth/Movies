from apps.movies.models import UserToken
from django.contrib.auth.models import User


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            token = UserToken.objects.get(token=token)
            request.user = token.user

        except Exception:
            pass
        
        response = self.get_response(request)
        return response
