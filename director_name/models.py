from django.db import models

class Director_name(models.Model):
	director_name_id=models.PositiveIntegerField(default=0)
	image_id=models.IntegerField(blank=False)


	class Meta:
		verbose_name_plural="director name"