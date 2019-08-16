from django.db import models

# Create your models here.
class Season(models.Model):
	season_id=models.IntegerField()
	season_no=models.IntegerField()
	season_name=models.TextField(default=None)
	episode_id=models.IntegerField()
	plot=models.TextField(default=None)

	def __str__(self):
		return self.season_name
	class Meta:
		verbose_name_plural="season"
