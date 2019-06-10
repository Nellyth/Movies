from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from apps.movies.forms import UserForm, MoviesForm
from apps.movies.models import Movie


class signup(CreateView):
    model = User
    template_name = 'Register_user.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class register_movie(CreateView):
    model = Movie
    template_name = 'register_movie.html'
    form_class = MoviesForm
    success_url = reverse_lazy('index')