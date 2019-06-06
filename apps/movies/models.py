from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False)
    duration = models.TimeField(null=False)
    poster = models.ImageField(upload_to = 'static/image', null=False)
    detail = models.TextField(null=False, max_length=150)
    trailer_url = models.URLField(null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=False)
    genre = models.ForeignKey('Genre', null=False, on_delete=models.CASCADE)
    original_language = models.ForeignKey('Language', null=False, on_delete=models.CASCADE)
    country = models.ForeignKey('Country', null=False, on_delete=models.CASCADE)
    directors = models.ForeignKey('MovieDirector', null=False, on_delete=models.CASCADE)
    actors = models.ForeignKey('MovieActor', null=False, on_delete=models.CASCADE)


class MovieRate(models.Model):
    movie = models.ForeignKey('Movie', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    comment = models.TextField(null=False, max_length=150)


class MovieActor(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False)
    age = models.IntegerField(null=False)


class MovieDirector(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False)
    age = models.IntegerField(null=False)


class Genre(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)


class Language(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)


class Country(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)
