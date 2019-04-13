from django.db import models
from django.conf import settings


# Create your models here.

class Movie(models.Model):

    name = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.movie.name
