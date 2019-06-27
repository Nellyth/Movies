import django_filters
from django_filters.rest_framework import FilterSet
from apps.movies.choices import movie_genre


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    # genre = django_filters.MultipleChoiceFilter(field_name='genre', lookup_expr='icontains', choices=movie_genre,
    #                                            conjoined=True)
    genre = django_filters.MultipleChoiceFilter(field_name='genre', lookup_expr='icontains', choices=movie_genre)
