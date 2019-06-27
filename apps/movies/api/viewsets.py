import django_filters
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.movies.api.filters import MovieFilter
from apps.movies.api.pagination import CustomPagination
from apps.movies.api.permissions import PermissionsRate
from apps.movies.api.serializers import MovieSerializer, MovieRateSerializer, MovieSerializer2
from apps.movies.models import Movie, MovieRate
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ExampleViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response({'Action': 'List'})

    def retrieve(self, request, pk=None):
        return Response({'Action': 'Retrieve'})

    def create(self, request):
        return Response({'Action': 'Create'})

    def update(self, request, pk=None):
        return Response({'Action': 'Update'})

    def destroy(self, request, pk=None):
        return Response({'Action': 'Destroy'})


class MovieDetailView2(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class MovieRateListView(ListAPIView):
    queryset = MovieRate.objects.all()
    serializer_class = MovieRateSerializer


class MovieRateDetailView(RetrieveAPIView):
    queryset = MovieRate.objects.all()
    serializer_class = MovieRateSerializer


class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer2


class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer2


class CreateListRetrieveUpdateDestroyViewSet(mixins.CreateModelMixin,
                                             mixins.ListModelMixin,
                                             mixins.RetrieveModelMixin,
                                             mixins.DestroyModelMixin,
                                             mixins.UpdateModelMixin,
                                             viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer2


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_classes = {
        'rate': MovieRateSerializer,
        'default': MovieSerializer2
    }
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = MovieFilter
    pagination_class = CustomPagination

    def get_serializer_class(self):
        return self.serializer_classes[self.action] if self.action in self.serializer_classes.keys() else \
            self.serializer_classes['default']

    def get_serializer_context(self):
        context = super(MovieViewSet, self).get_serializer_context()
        context.update({'request': self.request})
        return context

    @action(methods=['POST'], detail=True)
    def rate(self, request, pk=None):
        obj = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=obj, user=request.user)

        return Response(data=self.get_serializer(serializer.instance).data)


class MovieRateViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = MovieRate.objects.all()
    serializer_class = MovieRateSerializer
    permission_classes = [PermissionsRate, ]
