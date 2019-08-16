
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.db import models
from award_list.models import Award_list
from award_name.models import Award_name
from cast.models import Cast
from country_list.models import Country_list
from director.models import Director
# from episode.models import Episode
from genre_list.models import Genre_list
from genre_name.models import Genre_name
from language_name.models import Language_name
from links.models import Link
from pics.models import Pics
from season.models import Season
from server_name.models import Server_name
from server_type.models import Server_type
from subtitle_list.models import Subtitle_list
from subtitle_name.models import Subtitle_name
from writer.models import Writer
# Create your models here.
class Movies_list(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.TextField(blank=False,null=False)
	genre_list_id=models.IntegerField(blank=False,null=False)
	cast_id=models.IntegerField()
	director_id=models.IntegerField()
	writer_id=models.IntegerField()
	country_id=models.IntegerField(default=1)
	story_line=models.TextField()
	season_id=models.IntegerField(blank=True)
	cost=models.IntegerField()
	award_id=models.IntegerField()
	release=models.DateField(auto_now=False, auto_now_add=False)
	created_at=models.DateTimeField(auto_now=True, auto_now_add=False)
	language_id=models.IntegerField(default=25)
	imdb_ratting=models.FloatField()
	trailer_link=models.TextField()
	views=models.IntegerField(default=0)
	likes=models.IntegerField(default=0)
	ratting=models.FloatField(default=0.0)
	imdb_link=models.TextField()
	tags=models.TextField()


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "movies_list"







