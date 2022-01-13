from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField(null=True, blank=True)
    is_activate = models.BooleanField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.name


STARS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Rating(models.Model):
    text = models.CharField(max_length=100)
    stars = models.IntegerField(choices=STARS)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='rating')

    def __str__(self):
        return self.text
