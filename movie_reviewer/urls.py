from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout, password_change
from axes.decorators import watch_login
from movie_reviewer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login', watch_login(views.login), name ='login'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^createuser', views.create_user, name='createuser'),
    url(r'^movie/(?P<movie_id>\d+)', views.view_movie, name='movie'),
    url(r'^add-movie', views.add_movie, name='addmovie'),
    url(r'^review', views.review, name='review'),
    url(r'^latest-reviews', views.latest_reviews, name='latestReviews'),
    url(r'^search/search_term', views.search, name='search'),
    url(r'^logout', views.logout, name='logout'),
)