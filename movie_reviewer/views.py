from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from movie_reviewer.models import *


def index(request):
    hot_or_not = Movie.objects.all()
    template = loader.get_template('reviewer/index.html')
    context = RequestContext(request, {
        'hot_or_not': hot_or_not,
    })
    return HttpResponse(template.render(context))


def login(request):
    return HttpResponse("This will be login page")


def user(request):
    return HttpResponse("This will be users page")


def create_user(request):
    return HttpResponse("This is where you create a user")


def add_movie(request):
    return HttpResponse("This is where you add a movie")


def view_movie(request, movie_id):
    movie_film = get_object_or_404(Movie, id=movie_id)
    template = loader.get_template('reviewer/movie.html')
    context = RequestContext(request, {
        'movie': movie_film,
    })

    return HttpResponse(template.render(context) )


def review(request):
    return HttpResponse("This is where you create a review")


# Create your views here.
