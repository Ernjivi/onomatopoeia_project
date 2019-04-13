import json

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from reviews.models import Movie
from reviews.forms import ReviewForm

from django.views.generic import ListView, DetailView


@method_decorator(login_required, name='dispatch')
class Index(ListView):
    model = Movie
    template_name = 'index.html'


@method_decorator(login_required, name='dispatch')
class MovieDetial(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super(MovieDetial, self).get_context_data(**kwargs)
        context.update({'review_form': ReviewForm()})
        return context


@require_POST
@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.movie = movie
        review.save()
        if request.is_ajax():
            return HttpResponse(json.dumps({'author': review.author, 'body': review.body }), status=200)
        return HttpResponseRedirect(reverse('movie-detail', args=[movie_id]))




