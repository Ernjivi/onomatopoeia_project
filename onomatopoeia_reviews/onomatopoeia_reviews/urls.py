from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.http import HttpResponse

from reviews.views import Index, movie_detail, add_review



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('movie-detail/<movie_id>/', movie_detail, name='movie-detail'),
    path('add-review/<movie_id>/', add_review, name='add-review'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
