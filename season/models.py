from django.db import models

# Create your models here.
class season(models.Model):
	season_id=models.SmallIntegerField()
	season_name=models.TextField(blank=False)
	eposide_id=models.PositiveIntegerField()
	plot=models.TextField()
