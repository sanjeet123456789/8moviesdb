from django.db import models
from award_list.models import Award_list
from award_name.models import Award_name
from cast.models import Cast
from director.models import Director
from episode.models import Episode
from genre_list.models import Genre_list
from genre_name.models import Genre_name
from language_name.models import Language_name
from links.models import Link
from pics.models import Pics
from season.models import Season
from writer.models import Writer
# Create your models here.
class Movies_list(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.TextField(blank=False,null=False)
	genres_list_id=models.IntegerField(blank=False,null=False)
	cast_id=models.IntegerField()
	director_id=models.IntegerField()
	writer_id=models.IntegerField()
	country_id=models.IntegerField()
	story_line=models.TextField()
	season_id=models.IntegerField(blank=False)
	cost=models.IntegerField()
	Awards_id=models.IntegerField()
	Release=models.DateField(auto_now=False, auto_now_add=False)
	created_at=models.DateTimeField(auto_now=True, auto_now_add=False)
	language_id=models.IntegerField()
	IMDB_ratting=models.FloatField()
	trailer_link=models.TextField()
	views=models.IntegerField()
	likes=models.IntegerField()
	ratting=models.FloatField()
	imdb_link=models.TextField()
	tags=models.TextField()


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "movies_list"







