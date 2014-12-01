from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class Movie(models.Model):
    movie_title = models.CharField(max_length = 100)
    release_date = models.DateField('Date Released')
    director_first_name = models.CharField(max_length = 25)
    director_last_name = models.CharField(max_length = 25)
    lead_actor = models.CharField(max_length=50,blank=True, null=True)
    genre = models.CharField(default='action',max_length = 25)
    runtime = models.PositiveIntegerField(default = 0 )
    synopsis = models.CharField(max_length = 2500)
    avg_score = models.FloatField(default = 5, editable = False)
    movie_image = models.ImageField(max_length= 2500, null=True, blank=True)
# look into persisting images as blobs

    def __str__(self):
        return self.movie_title
    def hot_or_not(self):
        return self.avg_score > 6




class ReviewUser(models.Model):
    user_name = models.CharField(max_length = 25, unique = True, null = False)
    email = models.EmailField(max_length = 50, unique = True, null = False)
    user_since = models.DateField('Registration Date')
    favorite_movie = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user_name

class Review(models.Model):
    movie = models.ForeignKey(Movie)
    movie_rating = models.IntegerField(default = 5)
    movie_comments = models.CharField(max_length = 5000)
    review_post_date =  models.DateField('Date Posted')
    reviewer = models.ForeignKey( ReviewUser )

    def __str__(self):
        review_id = self.movie.movie_title + " review done by: " + self.reviewer.user_name
        return review_id
    def average_score(movie_rated):
        if isinstance(movie_rated, Movie):
            avg = 0
            count= 0
            reviews =  Review.objects.filter(movie=movie_rated)
            for review in reviews:
                avg = avg + review.movie_rating
                count += 1
            movie_rated.avg_score = avg / count
            movie_rated.save()
            return avg/count
    class Meta:
        ordering = ['-review_post_date']


class Actor(models.Model):
    movie = models.ManyToManyField(Movie)
    actor_first_name = models.CharField(max_length = 25)
    actor_last_name = models.CharField(max_length = 25)

    def __str__(self):
        actor = self.actor_last_name + " " + self.actor_first_name
        return actor


class NewsArticle(models.Model):
    article_title = models.CharField(max_length = 100)
    article_post_date =  models.DateField('Date Posted')
    article_synopsis = models.CharField(max_length = 100)
    article_full_text = models.CharField(max_length = 20000)
    article_poster = models.ForeignKey( ReviewUser )

    def __str__(self):
        return self.article_title
    class Meta:
        ordering = ['-article_post_date']

