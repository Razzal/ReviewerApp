from django.conf.urls import patterns, url

from movie_reviewer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name ='login'),
    url(r'^users', views.user, name='user'),
    url(r'^createuser', views.create_user, name='createuser'),
    url(r'^movie/(?P<movie_id>\d+)', views.view_movie, name='movie'),
    url(r'^addmovie', views.add_movie, name='addmovie'),
    url(r'^review', views.review, name='review'),
)