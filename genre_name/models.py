from django.db import models

class Genre_name(models.Model):
	genre_name_id=models.IntegerField()
	genre_name=models.CharField(max_length=40)

	def __str__(self):
		return self.genre_name
	class meta:
		verbose_name_plural="genre_name"