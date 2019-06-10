from django.conf.urls import url
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path
from django.views.generic import TemplateView
from apps.movies.views import SignUp, register_movie

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'accounts/login', LoginView.as_view(template_name='index.html'), name="login"),
    url(r'logout', logout_then_login, name='logout'),
    url(r'register_user', SignUp.as_view(), name='register_user'),
    url(r'register_movie', register_movie.as_view(), name='register_movie')
]
