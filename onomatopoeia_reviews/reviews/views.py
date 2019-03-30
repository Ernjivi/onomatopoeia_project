from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse

from reviews.models import Movie
from reviews.forms import ReviewForm



def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'review_form': review_form
    }
    return render(request, 'movie-detail.html', context)

@require_POST
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.movie = movie
        review.save()
        return HttpResponseRedirect(reverse('movie-detail', args=[movie_id]))

