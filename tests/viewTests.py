from django.test import SimpleTestCase
from movie_reviewer.models import *
from movie_reviewer.account import *
from django.test import Client

class ASetUp(SimpleTestCase):
    def setUp(self):
        newuser = User.objects.create_user(username='MrAwesome',password='somepass')
        newuser.save()
        ReviewUser.objects.create(user_name = "MrAwesome", email = "ladida@aol.com", user_since = "2014-01-01", favorite_movie = "Suicide Club", user = User.objects.get_by_natural_key('MrAwesome') )
        Movie.objects.create(movie_title ="MovieFilm", release_date = "2014-01-01", director_first_name = "Yolo", director_last_name = "Swag", lead_actor = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)
        reviewer = ReviewUser.objects.get(user_name='MrAwesome')
        movie = Movie.objects.get(movie_title='MovieFilm')
        Review.objects.create(movie = movie, movie_rating = 8, movie_comments = "This is a movie, score 8",review_post_date = "2014-03-03", reviewer=reviewer)
        NewsArticle.objects.create(article_title ='NEWS1',article_post_date="2014-02-03", article_synopsis='A news article1', article_full_text='This is not a long article1', article_poster=reviewer)
        NewsArticle.objects.create(article_title ='NEWS2',article_post_date="2014-01-01", article_synopsis='A news article2', article_full_text='This is not a long article2', article_poster=reviewer)
        NewsArticle.objects.create(article_title ='NEWS3',article_post_date="2014-01-01", article_synopsis='A news article3', article_full_text='This is not a long article3', article_poster=reviewer)
        NewsArticle.objects.create(article_title ='NEWS4',article_post_date="2014-01-01", article_synopsis='A news article4', article_full_text='This is not a long article4', article_poster=reviewer)
        NewsArticle.objects.create(article_title ='NEWS5',article_post_date="2014-01-01", article_synopsis='A news article5', article_full_text='This is not a long article5', article_poster=reviewer)

class IndexTests(SimpleTestCase):

    def testIndex(self):
        client = Client()
        response = client.get('/reviewer/')
        self.assertTemplateUsed(response, 'reviewer/index.html')

class LoginTests(SimpleTestCase):

    def testLoginRedirect(self):
        client = Client()
        response = client.get('/reviewer/review')
        self.assertRedirects(response, '/reviewer/login?next=/reviewer/review')
        client.login(username='MrAwesome',password='somepass')


