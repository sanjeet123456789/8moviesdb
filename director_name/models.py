from django.db import models

class Director_name(models.Model):
	director_name_id=models.PositiveIntegerField()
	director_name=models.CharField(max_length=40)
	image_id=models.IntegerField(default=None)


	class Meta:
		verbose_name_plural="director name"