from django.test import TestCase
from movie_reviewer.models import *
from movie_reviewer.account import *

class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(movie_title ="MovieFilm", release_date = "01/01/2014", director_first_name = "Yolo", director_last_name = "Swag", lead_actore = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)

    def movieGetTest(self):
        """Verify the movie is created and assert values are correct"""
        movie = Movie.objects.get(movie_title = "MovieFilm")

        self.assertEqual(movie.release_date, "01/01/2014")
        self.assertEqual(movie.director_first_name, "Yolo")
        self.assertEqual(movie.director_last_name, "Swag")
        self.assertEqual(movie.lead_actor, "Tom Cruise")
        self.assertEqual(movie.genre,"crap")
        self.assertEqual(movie.runtime, 100)
        self.assertEqual(movie.synopsis, "It is another action movie")
        self.assertEqual(movie.avg_score, 5)

class ReviewUserTest(TestCase):
    def setUp(self):
        testUser = User()
        ReviewUser.objects.create(user_name = "Awesome", email = "ladida@aol.com", user_since = "01/01/1901", favorite_movie = "Suicide Club", user = testUser )

    def reviewUserGetTest(self):
        """Verify the reviewuser is created and assert the values are correct"""

        review_user = ReviewUser.objects.get(user_name = "Awesome")
        
        self.assertEqual(review_user.email ,"ladida@aol.com")
        self.assertEqual(review_user.user_since, "01/01/1901")

class ReviewTest(TestCase):
    def setUp(self):
         movie = Movie.objects.create(movie_title ="MovieFilm", release_date = "01/01/2014", director_first_name = "Yolo", director_last_name = "Swag", lead_actore = "Tom Cruise", genre = "crap", runtime = 100, synopsis = "It is another action movie", avg_score=5)
         testUser = User()
         ReviewUser.objects.create(user_name = "Awesome", email = "ladida@aol.com", user_since = "01/01/1901", favorite_movie = "Suicide Club", user = testUser )
         Review.objects.create(movie = movie, movie_rating = 8, movie_comments = "This is a movie",review_post_date = "02/03/2014")