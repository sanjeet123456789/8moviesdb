from django.db import models

class Genre_list(models.Model):
	genre_id=models.IntegerField()
	genre_no=models.IntegerField()
	genre_name_id=models.IntegerField()
	
	class Meta:
		verbose_name_plural= "genre_list"


