from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from apps.movies.forms import UserForm, MoviesForm, RatingMoviesForm
from apps.movies.models import Movie, MovieRate


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
        return qs


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


class RegisterMovieRating(LoginRequiredMixin, CreateView):
    model = MovieRate
    template_name = 'rating_movie.html'
    form_class = RatingMoviesForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form.user = User.objects.get(pk=request.user.id)
        form.movie = Movie.objects.get(pk=request.POST.get('movie'))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
