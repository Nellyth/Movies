from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.movies.models import MovieRate, Movie


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=False)
    poster = serializers.ImageField(required=True)
    detail = serializers.CharField(required=False)
    trailer_url = serializers.URLField(required=True)
    genre = serializers.CharField(required=False)
    release_date = serializers.DateField(required=True, input_formats=['%d/%m/%Y'])
    slug = serializers.CharField(required=True)


class MovieRateSerializer(ModelSerializer):
    pk = serializers.IntegerField(source='id', read_only=True)
    user = serializers.StringRelatedField()
    movie = serializers.HyperlinkedRelatedField(read_only=True,
                                                view_name='movie_detail_view2',
                                                lookup_field='slug',
                                                lookup_url_kwarg='slug')

    class Meta:
        model = MovieRate
        fields = ['movie', 'user', 'pk', 'rating', 'comment']


class MovieSerializer2(ModelSerializer):
    pk = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Movie
        fields = [
            'pk',
            'title',
            'duration',
            'poster',
            'detail',
            'trailer_url',
            'genre',
            'release_date',
        ]
