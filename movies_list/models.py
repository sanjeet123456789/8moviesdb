from django.db import models

# Create your models here.
class movies_list(models.Model):
	name=models.TextField(max_length=500,blank=False,null=False)
	genres_list=models.TextField(blank=False,null=False)
	cast_id=models.TextField(blank=False,null=False)
	director_id=models.TextField(blank=False,null=False)
	writer_id=models.TextField
	country=
	story_line=
	season_id=
	cost=
	Awards=
	Release=
	language=
	IMDB_ratting=
	trailer_link=
	views=
	likes=
	ratting=
	tags=






