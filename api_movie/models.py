from django.db import models
from datetime import date


class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=25, blank=True)
    Rated = models.CharField(max_length=10, blank=True)
    Released = models.CharField(max_length=25, blank=True)
    Runtime = models.CharField(max_length=25, blank=True)
    Genre = models.CharField(max_length=200, blank=True)
    Director = models.CharField(max_length=100, blank=True)
    Writer = models.CharField(max_length=300, blank=True)
    Actors = models.CharField(max_length=500, blank=True)
    Plot = models.CharField(max_length=900, blank=True)
    Language = models.CharField(max_length=300, blank=True)
    Country = models.CharField(max_length=100, blank=True)
    Awards = models.CharField(max_length=250, blank=True)
    Poster = models.URLField(blank=True)
    Metascore = models.CharField(max_length=5, blank=True)
    imdbRating = models.CharField(max_length=5, blank=True)
    imdbVotes = models.CharField(max_length=100, blank=True)
    imdbID = models.CharField(max_length=100, blank=True)
    Type = models.CharField(max_length=10, blank=True)
    DVD = models.CharField(max_length=25, blank=True)
    BoxOffice = models.CharField(max_length=25, blank=True)
    Production = models.CharField(max_length=100, blank=True)
    Website = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.Title


class Rating(models.Model):
    Source = models.CharField(max_length=50, blank=True)
    Value = models.CharField(max_length=20, blank=True)
    Movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="Ratings")

    def __str__(self):
        return f'Rating from {self.Source} to {self.Movie.Title}'


class Comment(models.Model):
    comment_text = models.CharField(max_length=200)
    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='Comments')
    pub_date = models.DateField(blank =True, default=date.today)

    def __str__(self):
        return f" Comment for {self.movie_id} (id: {self.movie_id.id}): {self.comment_text}"
