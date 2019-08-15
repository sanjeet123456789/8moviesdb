from django.db import models

# Create your models here.
class Director(models.Model):
	director_id=models.IntegerField()
	director_no=models.IntegerField()
	director_name_id=models.PositiveIntegerField()
	

	class Meta:
		verbose_name_plural = "director"

