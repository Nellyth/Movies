from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from celery import chord
from apps.movies.api.serializers import MovieSerializer
from apps.movies.forms import UserForm, MoviesForm, RatingMoviesForm, QueryMovieForm
from apps.movies.models import Movie, MovieRate
from django.conf import settings
from django.shortcuts import resolve_url
from django.contrib.auth import login as auth_login
from rest_framework.renderers import JSONRenderer

from apps.movies.tasks import query_movies, send_email


class Index(ListView):
    template_name = 'index.html'
    queryset = Movie.objects.all()
    paginate_by = 5

    def get_queryset(self):
        qs = super(Index, self).get_queryset()
        return qs.order_by('-id')


class SignUp(CreateView):
    model = User
    template_name = 'index.html'
    form_class = UserForm
    success_url = reverse_lazy('index')


class RegisterMovie(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'register_movie.html'
    form_class = MoviesForm
    success_url = reverse_lazy('index')


class MovieList(LoginRequiredMixin, ListView):
    template_name = 'list_movie.html'
    queryset = Movie.objects.all()

    def get_queryset(self):
        qs = super(MovieList, self).get_queryset()
        return qs.order_by('-id')


class SearchMovieList(ListView):
    template_name = 'list_movie.html'
    queryset = Movie.objects.all()

    def get_queryset(self):
        qs = super(SearchMovieList, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            qs = Movie.objects.filter(title__icontains=query)
        return qs.order_by('-id')


class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = 'register_movie.html'
    form_class = MoviesForm
    success_url = reverse_lazy('index')


class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'delete_movie.html'
    success_url = reverse_lazy('movie_list')


class MovieDetail(DetailView):
    model = Movie
    template_name = 'detail_movie.html'
    second_form_class = RatingMoviesForm
    slug_field = 'slug'
    query_pk_and_slug = False

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context


class RegisterMovieRating(LoginRequiredMixin, CreateView):
    model = MovieRate
    template_name = 'rating_movie.html'
    form_class = RatingMoviesForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class LoginViewModified(LoginView):

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        # UserToken.objects.get_or_create(user=self.request.user, defaults={'user': self.request.user})
        # data = UserToken.objects.get(user=self.request.user)
        Token.objects.get_or_create(user=self.request.user,
                                    defaults={'user': self.request.user})
        return HttpResponseRedirect(self.get_success_url())


def logout_then_login_modified(request, login_url=None):
    login_url = resolve_url(login_url or settings.LOGIN_URL)
    try:
        # UserToken.objects.filter(user=request.user).delete()
        Token.objects.filter(user=request.user).delete()
    except Exception:
        pass
    return LogoutView.as_view(next_page=login_url)(request)


class QueryMovieView(FormView):
    template_name = 'query_movies.html'
    form_class = QueryMovieForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        movie = form.cleaned_data['query']
        movie = movie.split(',')
        user = {'username': self.request.user.username, 'email': self.request.user.email}
        if len(movie) > 1:
            callback = send_email.s(user=user)
            header = [query_movies.s(mov.strip()) for mov in movie]
            chord(header)(callback)
        else:
            chord(query_movies.s(movie))(send_email.s(user=user))
        return super().form_valid(form)


class MovieListView(ListView):
    model = Movie
    content_type = 'application/json'
    response_class = HttpResponse

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MovieListView, self).get_context_data(object_list=object_list, **kwargs)
        context.update({'serializer_data': JSONRenderer().render(MovieSerializer(self.get_queryset(), many=True).data)})
        return context

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(context.get('serializer_data'), **response_kwargs)


class MovieDetailView(DetailView):
    model = Movie
    content_type = 'application/json'
    response_class = HttpResponse
    slug_field = 'slug'
    query_pk_and_slug = False

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['object'] = self.object
        context.update({'serializer_data': JSONRenderer().render(MovieSerializer(self.object).data)})
        return super().get_context_data(**context)

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(context.get('serializer_data'), **response_kwargs)
