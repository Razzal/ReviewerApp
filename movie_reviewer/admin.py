from django.contrib import admin
from movie_reviewer.models import Movie, User, Actors, Review

admin.site.register(Movie)

admin.site.register(User)

admin.site.register(Review)