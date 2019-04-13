from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from reviews.models import Movie, Review
from reviews.serializers import MovieSerializer, ReviewSerializer


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        qs = super(MovieListCreateAPIView, self).get_queryset()
        search = self.request.GET.get('search', None)
        if search:
            qs = qs.filter(name__icontains=search)
        return qs


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ['movie']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
