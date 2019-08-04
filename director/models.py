from django.db import models

# Create your models here.
class director(models.Model):
	director_name=models.CharField(max_length=40,blank=False)
	image_id=models.PositiveSmallIntegerField()
