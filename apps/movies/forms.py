from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from apps.movies.models import Movie
from apps.movies.choices import movie_genre, movie_rating


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

        label = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Password Confirmation',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title',
            'duration',
            'poster',
            'detail',
            'trailer_url',
            'rating',
            'genre',
            'original_language',
            'country',
            'directors',
            'actors'
        ]

        labels = {
            'title': 'Title',
            'duration': 'Duration',
            'poster': 'Poster',
            'detail': 'Detail',
            'trailer_url': 'Trailer url',
            'rating': 'Rating',
            'genre': 'Genre',
            'original_language': 'Original language',
            'country': 'Country',
            'directors': 'Directors',
            'actors': 'Actors'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=movie_genre, attrs={'class': 'form-control'}),
            'genre': forms.Select(choices=movie_rating, attrs={'class': 'form-control'}),
            'original_language': forms.Select(),
            'country': forms.Select(),
            'directors': forms.Select(),
            'actors': forms.Select(),
        }