from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from movie_reviewer.models import *
from movie_reviewer.reviewer_forms import *
from django.contrib.auth.decorators import login_required
from movie_reviewer.account import *
import datetime

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
    status_message=''
    if request.method == 'POST:':
        add_movie_form = AddMovieForm(request.POST)
        if add_movie_form.is_valid():
            movie = Movie()
            movie.movie_title = add_movie_form.cleaned_data['movie']
            movie.release_date = add_movie_form.cleaned_data['release_date']
            movie.director_first_name = add_movie_form.cleaned_data['director_first']
            movie.director_last_name = add_movie_form.cleaned_data['director_last']
            movie.lead_actor = add_movie_form.cleaned_data['lead_first'] + ' ' + add_movie_form.cleaned_data['lead_last']
            movie.genre = add_movie_form.cleaned_data['genre']
            movie.runtime = add_movie_form.cleaned_data['runtime']
            movie.synopsis = add_movie_form.cleaned_data['synopsis']
            movie.avg_score=5
            print(movie.save())
            status_message='Movie Added Successfully'
            return render(request, 'reviewer/add_movie.html', {'add_movie_form': add_movie_form, 'message': status_message})
        else:
            status_message="Missing required fields"
            return render(request, 'reviewer/add_movie.html', {'add_movie_form': add_movie_form, 'message': status_message})
    else:
        add_movie_form = AddMovieForm()
    return render(request, 'reviewer/add_movie.html', {'add_movie_form': add_movie_form})


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
    status_message=''
    if request.method == 'POST':
        add_review_form = AddReviewForm(request.POST)

        if add_review_form.is_valid():
            review = Review()
            review.movie= add_review_form.cleaned_data['movie']
            review.movie_rating = add_review_form.cleaned_data['movie_rating']
            review.movie_comments = add_review_form.cleaned_data['movie_comments']
            review.review_post_date = datetime.date.today()
            review.reviewer =get_object_or_404(ReviewUser, user = request.user)
            review.save()
            status_message="Review successfully saved"
            return render(request, 'reviewer/add_review.html', {'add_review_form': add_review_form, 'message': status_message})
    else:
        add_review_form = AddReviewForm()
    return render(request, 'reviewer/add_review.html', {'add_review_form': add_review_form})


def latest_reviews(request):
    review_list = Review.objects.all()
    template = loader.get_template('reviewer/latest_reviews.html')
    context = RequestContext(request, {
        'hot_or_not':review_list,
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
