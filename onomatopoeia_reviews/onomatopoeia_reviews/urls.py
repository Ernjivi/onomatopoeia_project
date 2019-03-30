from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

from reviews.views import index, movie_detail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('movie-detail/<movie_id>/', movie_detail, name='movie-detail'),
]
