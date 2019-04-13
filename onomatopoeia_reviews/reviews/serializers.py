from rest_framework import serializers
from reviews.models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['name', 'review_count', 'release_date', 'director']


class ReviewSerializer(serializers.ModelSerializer):
    # movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['movie', 'body']
