import datetime 

from django.db import models
from django.utils import timezone
# Create your models here.

class Movie(models.Model):
    movie_text = models.CharField(max_length=200)
    seen = models.BooleanField(default = False)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self): 
    	return self.movie_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    	
class Choice(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1, default = '1')
    votes = models.IntegerField(default=0)


    def __str__(self): 
    	return self.choice_text

    