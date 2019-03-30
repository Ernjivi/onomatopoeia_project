from django.shortcuts import render

from reviews.models import Movie



def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movie-detail.html', context)
