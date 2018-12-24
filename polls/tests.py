from django.test import TestCase
from .models import Movie 
# Create your tests here.

class MovieMethodTests(TestCase): 

	def movie_has_zero_when_no_votes(self): 
		movie = Movie(movie_text='Blarg')
		self.assertEqual(movie.score, 0)

