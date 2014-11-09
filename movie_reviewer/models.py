from django.db import models
from django.core import validators


class Movie(models.Model):
    movie_title = models.CharField(max_length = 100)
    release_date = models.DateField('Date Released')
    director_first_name = models.CharField(max_length = 25)
    director_last_name = models.CharField(max_length = 25)
    genre = models.CharField(default='action',max_length = 25)
    runtime = models.PositiveIntegerField(default = 0 )
    synopsis = models.CharField(max_length = 2500)
    avg_score = models.FloatField(default = 5, editable = False)
    movie_image = models.ImageField(max_length= 2500, null=True)

    def __str__(self):
        return self.movie_title
    def hot_or_not(self):
        return self.avg_score > 6




class User(models.Model):
    user_name = models.CharField(max_length = 25, unique = True, null = False)
    password = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, unique = True, null = False)
    user_since = models.DateField('Registration Date')

    def __str__(self):
        return self.user_name

class Review(models.Model):
    movie = models.ForeignKey(Movie)
    movie_rating = models.IntegerField(default = 5)
    movie_comments = models.CharField(max_length = 2500)
    reviewer = models.ForeignKey( User )

    def __str__(self):
        review_id = self.movie.movie_title + " review done by: " + self.reviewer.user_name
        return review_id

class Actors(models.Model):
    movie = models.ForeignKey(Movie)
    actor_first_name = models.CharField(max_length = 25)
    actor_last_name = models.CharField(max_length = 25)

    def __str__(self):
        actor = self.actor_last_name + " " + self.actor_first_name
        return actor


