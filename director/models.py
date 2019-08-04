from django.db import models

# Create your models here.
class Director(models.Model):
	director_id=models.PositiveSmallIntegerField()
	director_name=models.CharField(max_length=40,blank=False)
	image_id=models.PositiveSmallIntegerField()
	
	def __str__(self):
		return self.director_name
	class Meta:
		verbose_name_plural = "director"

