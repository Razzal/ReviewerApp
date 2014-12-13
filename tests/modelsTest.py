from django.test import SimpleTestCase

from movie_reviewer.models import *
from movie_reviewer.account import *

class ArticleTest(SimpleTestCase):
    def setUp(self):
        User.objects.create_user(username='MrAwesome',password='somepass')
        ReviewUser.objects.create(user_name = "MrAwesome", email = "ladida@aol.com", user_since = "2014-01-01", favorite_movie = "Suicide Club", user = User.objects.get_by_natural_key('MrAwesome') )
        Movie.objects.create(movie_title ="MovieFilm", release_date = "2014-01-01", director_first_name = "Yolo", director_last_name = "Swag", lead_actor = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)
        Movie.objects.create(movie_title ="MovieFilm2", release_date = "2014-01-01", director_first_name = "Yolo", director_last_name = "Swag", lead_actor = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)
        Movie.objects.create(movie_title ="MovieFilm3", release_date = "2014-01-01", director_first_name = "Yolo", director_last_name = "Swag", lead_actor = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)
        Movie.objects.create(movie_title ="MovieFilm4", release_date = "2014-01-01", director_first_name = "Yolo", director_last_name = "Swag", lead_actor = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)
        Movie.objects.create(movie_title ="MovieFilm5", release_date = "2014-01-01", director_first_name = "Yolo", director_last_name = "Swag", lead_actor = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)
        Movie.objects.create(movie_title ="MovieFilm6", release_date = "2014-01-01", director_first_name = "Yolo", director_last_name = "Swag", lead_actor = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)
        reviewer = ReviewUser.objects.get(user_name='MrAwesome')
        movie = Movie.objects.get(movie_title='MovieFilm')
        Review.objects.create(movie = movie, movie_rating = 8, movie_comments = "This is a movie, score 8",review_post_date = "2014-03-03", reviewer=reviewer)
        Review.objects.create(movie = movie, movie_rating = 6, movie_comments = "This is a movie, score 6",review_post_date = "2014-03-03", reviewer=reviewer)
        Review.objects.create(movie = movie, movie_rating = 3, movie_comments = "This is a movie, score 3",review_post_date = "2014-03-03", reviewer=reviewer)
        Review.objects.create(movie = movie, movie_rating = 6, movie_comments = "This is a movie, score 6",review_post_date = "2014-03-03", reviewer=reviewer)
        NewsArticle.objects.create(article_title ='NEWS1',article_post_date="2014-02-03", article_synopsis='A news article1', article_full_text='This is not a long article1', article_poster=reviewer)
        NewsArticle.objects.create(article_title ='NEWS2',article_post_date="2014-01-01", article_synopsis='A news article2', article_full_text='This is not a long article2', article_poster=reviewer)
        NewsArticle.objects.create(article_title ='NEWS3',article_post_date="2014-01-01", article_synopsis='A news article3', article_full_text='This is not a long article3', article_poster=reviewer)
        NewsArticle.objects.create(article_title ='NEWS4',article_post_date="2014-01-01", article_synopsis='A news article4', article_full_text='This is not a long article4', article_poster=reviewer)
        NewsArticle.objects.create(article_title ='NEWS5',article_post_date="2014-01-01", article_synopsis='A news article5', article_full_text='This is not a long article5', article_poster=reviewer)
    def testArticles(self):
        testArticle = NewsArticle.objects.get(article_title='NEWS1')
        reviewer = ReviewUser.objects.get(user_name='MrAwesome')
        testArticles = NewsArticle.objects.all()
        """Verifying correct amount returned and then that meta correctly sorts list desc date"""
        self.assertEqual(len(testArticles),5)
        self.assertEqual(testArticles.first().article_title,'NEWS1')
        self.assertEqual(testArticle.article_title,'NEWS1')
        self.assertEqual(str(testArticle.article_post_date),'2014-02-03')
        self.assertEqual(testArticle.article_synopsis,'A news article1')
        self.assertEqual(testArticle.article_full_text,'This is not a long article1')
        self.assertEqual(testArticle.article_poster,reviewer)
class MovieTestCase(SimpleTestCase):

    def testMovieGet(self):
        """Verify the movie is created and assert values are correct"""
        movie = Movie.objects.get(movie_title = "MovieFilm")

        self.assertEqual(str(movie.release_date), "2014-01-01")
        self.assertEqual(movie.director_first_name, "Yolo")
        self.assertEqual(movie.director_last_name, "Swag")
        self.assertEqual(movie.lead_actor, "Tom Cruise")
        self.assertEqual(movie.genre,"crap")
        self.assertEqual(movie.runtime, 100)
        self.assertEqual(movie.synopsis, "It is another action movie")
        self.assertEqual(movie.avg_score, 5)
        self.assertEqual(len(Movie.objects.all()),6)

class ReviewUserTest(SimpleTestCase):

    def testReviewUserGet(self):
        """Verify the reviewuser is created and assert the values are correct"""
        review_user = ReviewUser.objects.get(user_name = "MrAwesome")

        self.assertEqual(review_user.email ,"ladida@aol.com")
        self.assertEqual(str(review_user.user_since), "2014-01-01")

class ReviewTest(SimpleTestCase):

    def testReviews(self):
        movie = Movie.objects.get(movie_title='MovieFilm')

        self.assertEqual(len(Review.objects.filter(movie=movie)),4)

