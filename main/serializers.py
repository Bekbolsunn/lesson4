from rest_framework import serializers
from .models import Movie, Genre, Rating


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = 'id text stars'.split()


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    rating = RatingSerializer(many=True)

    class Meta:
        model = Movie
        # fields = '__all__'
        # fields = 'id name'.split()
        fields = ['id', 'name', 'genres', 'rating']


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'descriptions', 'duration']
