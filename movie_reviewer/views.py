from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from movie_reviewer.models import *
from movie_reviewer.reviewer_forms import *


def index(request):
    hot_or_not = Movie.objects.all()
    template = loader.get_template('reviewer/index.html')
    context = RequestContext(request, {
        'hot_or_not': hot_or_not,
    })
    return HttpResponse(template.render(context))


def login(request):
    return HttpResponse("This will be login page")


def profile(request):
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

    return HttpResponse(template.render(context))


def review(request):
    return HttpResponse("This is where you create a review")


def latest_reviews(request):
    return HttpResponse('This is where latest reviews will go')


def search(request):
    if request.method == 'GET':

        form = SearchForm(request.GET)

        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            movie_film = get_object_or_404(Movie, movie_title=search_term)

            return HttpResponseRedirect('/reviewer/movie/%d' % movie_film.id)
        else:
            form = SearchForm()
            return render(request, '/reviewer/', {'form': form})


# Create your views here.
