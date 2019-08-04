from django.db import models
from cast.models import Cast
from director.models import Director
from episode.models import Episode
from links.models import Link
from pics.models import Pics
from season.models import Season
from writer.models import Writer
# Create your models here.
class Movies_list(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.TextField(blank=False,null=False)
	genres_list_id=models.TextField(blank=False,null=False)
	cast_id=models.TextField(blank=False,null=False)
	director_id=models.PositiveSmallIntegerField()
	writer_id=models.PositiveSmallIntegerField()
	country_id=models.PositiveSmallIntegerField()
	story_line=models.TextField()
	season_id=models.PositiveSmallIntegerField(blank=False)
	cost=models.IntegerField()
	Awards_id=models.PositiveSmallIntegerField()
	Release=models.DateField(auto_now=False, auto_now_add=False)
	created_at=models.DateTimeField(auto_now=True, auto_now_add=False)
	language_id=models.PositiveSmallIntegerField()
	IMDB_ratting=models.FloatField()
	trailer_link=models.TextField()
	views=models.IntegerField()
	likes=models.TextField()
	ratting=models.FloatField()
	tags=models.TextField()


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "movies_list"






