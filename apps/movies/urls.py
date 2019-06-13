from django.conf.urls import url
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path
from django.views.generic import TemplateView
from apps.movies.views import SignUp, RegisterMovie, Index, MovieList, MovieUpdate, MovieDelete, MovieDetail, \
    RegisterMovieRating, LoginViewModified, logout_then_login_modified

urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('', Index.as_view(), name='index'),
    path('accounts/login', LoginViewModified.as_view(template_name='index.html'), name="login"),
    path('logout', logout_then_login_modified, name='logout'),
    path('register_user', SignUp.as_view(), name='register_user'),
    path('register_movie', RegisterMovie.as_view(), name='register_movie'),
    path('movie_list', MovieList.as_view(), name='movie_list'),
    url(r'^movie_update/(?P<pk>\d+)$', MovieUpdate.as_view(), name='movie_update'),
    url(r'^movie_delete/(?P<pk>\d+)$', MovieDelete.as_view(), name='movie_delete'),
    url(r'^movie_detail/(?P<pk>\d+)$', MovieDetail.as_view(), name='movie_detail'),
    path('register_rating', RegisterMovieRating.as_view(), name='register_rating'),

]
