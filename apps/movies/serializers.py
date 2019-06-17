from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=False)
    poster = serializers.ImageField(required=True)
    detail = serializers.CharField(required=False)
    trailer_url = serializers.URLField(required=True)
    genre = serializers.CharField(required=False)
    release_date = serializers.DateField(required=True, input_formats=['%d/%m/%Y'])
    slug = serializers.CharField(required=True)
