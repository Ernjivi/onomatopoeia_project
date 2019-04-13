from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

from django.http import HttpResponse

from reviews.views import Index, MovieDetial, add_review


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', Index.as_view(), name='index'),
    # path('movie-detail/<pk>/', MovieDetial.as_view(), name='movie-detail'),
    # path('add-review/<movie_id>/', add_review, name='add-review'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
