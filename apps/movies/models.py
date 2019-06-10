from django.db import models
from django.conf import settings
from apps.movies.choices import movie_genre, movie_rating


def movie_directory_path(instance, filename):
    return f'movie/{instance.title}/{filename}'


class Movie(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False)
    duration = models.IntegerField(null=False)
    poster = models.ImageField(upload_to=movie_directory_path, null=False)
    detail = models.TextField(null=False, max_length=150)
    trailer_url = models.URLField(null=True, blank=True)
    rating = models.IntegerField(choices=movie_rating, null=False)
    genre = models.CharField(max_length=25, null=False, choices=movie_genre)
    original_language = models.ForeignKey('Language', null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey('Country', null=True, on_delete=models.SET_NULL)
    directors = models.ManyToManyField('MovieDirector')
    actors = models.ManyToManyField('MovieActor')

    def __str__(self):
        return self.title


class MovieRate(models.Model):
    movie = models.ForeignKey('Movie', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    comment = models.TextField(null=False, max_length=150)

    def __str__(self):
        return 'Movie: {}, User {}'.format(self.movie.title, self.user.username)


class MovieActor(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False)
    age = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name


class MovieDirector(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False)
    age = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)

    def __str__(self):
        return self.name
