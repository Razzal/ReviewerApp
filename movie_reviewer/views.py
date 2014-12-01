from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from movie_reviewer.models import *
from movie_reviewer.reviewer_forms import *
from django.contrib.auth.decorators import login_required



def index(request):
    articles = NewsArticle.objects.all()
    template = loader.get_template('reviewer/index.html')
    context = RequestContext(request, {
        'newsarticles': articles,
    })
    return HttpResponse(template.render(context))


def login(request):
    return HttpResponse("This will be login page")

@login_required
def profile(request):
    return HttpResponse("This will be users page")


def create_user(request):
    if request.method == 'POST':
        create_user_form = LoginForm(request.POST)

        if create_user_form.is_valid():
            return HttpResponse('valid form')
    else:
        create_user_form = LoginForm()
    return render(request, 'reviewer/create_user.html', {'create_user_form': create_user_form})

@login_required
def add_movie(request):
    return HttpResponse("This is where you add a movie")


def view_movie(request, movie_id):
    movie_film = get_object_or_404(Movie, id=movie_id)
    movie_avg = Review.average_score(movie_film)
    reviews = Review.objects.filter(movie = movie_film)
    template = loader.get_template('reviewer/movie.html')
    context = RequestContext(request, {
        'movie': movie_film,
        'avg_rating': movie_avg,
        'reviews': reviews,
    })

    return HttpResponse(template.render(context))

@login_required
def review(request):
    return HttpResponse("This is where you create a review")


def latest_reviews(request):
    movie_list = Movie.objects.all()
    template = loader.get_template('reviewer/latest_reviews.html')
    context = RequestContext(request, {
        'hot_or_not': movie_list,
    })
    return HttpResponse(template.render(context))


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
