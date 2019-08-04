from django.db import models

# Create your models here.
class cast(models.Model):
	cast_id=models.PositiveSmallIntegerField()
	cast_name=models.CharField(max_length=40,blank=False)
	actual_name=models.CharField(max_length=40,blank=False)
	role=models.CharField(max_length=40,blank=False)
	image_id=models.PositiveSmallIntegerField(blank=False)
