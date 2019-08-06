from django.db import models

class Genre_list(models.Model):
	genre_id=models.IntegerField()
	genre_name_id=models.IntegerField()

	def __str__(self):
		return self.genre_id

	class Meta:
		verbose_name_plural= "genre_list"


