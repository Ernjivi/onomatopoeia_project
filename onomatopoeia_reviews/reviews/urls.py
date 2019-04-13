from django.urls import path
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet, MovieListCreateAPIView

router = DefaultRouter()
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movies'),
]

urlpatterns += router.urls
