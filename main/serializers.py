from rest_framework import serializers
from .models import Movie, Genre, Rating
from rest_framework.exceptions import ValidationError


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = 'id text value'.split()


class MovieSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True)
    # ratings = RatingSerializer(many=True)
    ratings = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = '__all__'
        # fields = 'id name'.split()
        fields = ['id', 'name', 'genres', 'ratings', 'count_genres', 'rating']

    def get_ratings(self, movie):
        # rate = movie.ratings.filter(value__gt=3)
        return RatingSerializer(Rating.objects.filter(movie=movie, value__gt=3), many=True).data

    def get_genres(self, movie):
        return GenreSerializer(movie.genres.filter(is_active=True), many=True).data


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'duration', 'count_genres']


class GenreCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    is_active = serializers.BooleanField()


class MovieCreateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=10)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(default=8)
    is_active = serializers.BooleanField()
    genres = serializers.ListField(child=serializers.IntegerField())
    created_genres = serializers.ListField(child=GenreCreateSerializer())

    # """Русская раскласдка"""
    #
    # def validate_name(self, name):
    #     for i in name:
    #         if ord(i) >= 1040 and ord(i) <= 1103:
    #             raise ValidationError('Pleace use english only')
    #     return name

    # def validate_name(self, name):
    #     movies = Movie.objects.filter(name=name)
    #     if movies:
    #         raise ValidationError('Movie already exists!')
    #     return name

    def validate(self, attrs):
        name = attrs['name']
        movies = Movie.objects.filter(name=name)
        if movies:
            raise ValidationError('Movie already exists!')
        return name


