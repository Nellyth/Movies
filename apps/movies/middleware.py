from django.contrib.auth import logout

from apps.movies.models import UserToken
from django.shortcuts import redirect


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            try:
                UserToken.objects.get(user=request.user)
            except Exception:
                logout(request)
                response = redirect('logout')
                response.delete_cookie('user_location')
                return response

        if request.path == '/movie/logout':
            print('Se Ha Deslogueado')
        response = self.get_response(request)
        return response
