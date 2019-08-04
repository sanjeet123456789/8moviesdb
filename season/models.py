from django.db import models

# Create your models here.
class season(models.Model):
	season_id=models.SmallIntegerField()
	season_name=models.TextField(blank=False)
	eposide_id=models.PositiveIntegerField()
	plot=models.TextField()

	def __str__(self):
		return self.season_name
	class Meta:
		verbose_name_plural="season"
