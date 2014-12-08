from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from movie_reviewer.models import *
from movie_reviewer.reviewer_forms import *
from django.contrib.auth.decorators import login_required
from movie_reviewer.account import *

def index(request):
    articles = NewsArticle.objects.all()
    template = loader.get_template('reviewer/index.html')
    context = RequestContext(request, {
        'newsarticles': articles,
    })
    return HttpResponse(template.render(context))


@login_required
def profile(request):
    return HttpResponse("This will be users page")


def create_user(request):
    if request.method == 'POST':
        create_user_form = CreateUserForm(request.POST)

        if create_user_form.is_valid():
            account_to_create = Account()
            new_account_status = account_to_create.validate_new_user(create_user_form.cleaned_data['user_name'],create_user_form.cleaned_data['email'],create_user_form.cleaned_data['password'],create_user_form.cleaned_data['confirm_password'])
            if new_account_status == "True":
                account_to_create.create_account(create_user_form.cleaned_data['user_name'], create_user_form.cleaned_data['email'], create_user_form.cleaned_data['password'])
                new_account_status = "Account Created Successfully"

            return render(request, 'reviewer/create_user.html', {'create_user_form': create_user_form, 'message': new_account_status})
    else:
        create_user_form = CreateUserForm()
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

def logout(request):
    account = Account()
    account.logout(request)
    return HttpResponseRedirect('/reviewer/')

def login(request):
    status_message = ''
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            account = Account()
            user = account.login(login_form.cleaned_data['user_name'], login_form.cleaned_data['password'],request)
            if isinstance(user, User):
                review_user = ReviewUser.objects.filter(user = user)
                return render(request, 'reviewer/login.html', {'login_form': login_form, 'message': status_message})
    else:
            login_form = LoginForm()
    return render(request, 'reviewer/login.html', {'login_form': login_form})