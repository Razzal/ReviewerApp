from django.contrib import admin
from movie_reviewer.models import Movie, ReviewUser, Actor, Review, NewsArticle

admin.site.register(Movie)

admin.site.register(ReviewUser)

admin.site.register(Review)

admin.site.register(NewsArticle)

admin.site.register(Actor)