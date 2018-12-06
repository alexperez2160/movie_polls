import datetime 

from django.db import models
from django.utils import timezone
# Create your models here.

class Movie(models.Model):
    movie_text = models.CharField(max_length=200)
    rel_date = models.DateTimeField('Release Date')
    seen = models.BooleanField(default = False)
    score = models.IntegerField(default=0)
    
    def __str__(self): 
    	return self.movie_text
    def coming_soon(self): 
    	return self.rel_date - timezone.now() <= 7
    	
class Choice(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1, default = '1')
    votes = models.IntegerField(default=0)


    def __str__(self): 
    	return self.choice_text

    