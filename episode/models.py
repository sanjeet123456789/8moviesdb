from django.db import models

from django.db import models
# import datetime
# import time
# Create your models here.
class Episode(models.Model):
	episode_id=models.IntegerField(blank=False)
	episode_no=models.IntegerField()
	episode_name=models.CharField(max_length=40)
	link_list_id=models.IntegerField()

	views=models.IntegerField(default=0)
	adult=models.BooleanField(default=False)
	filler=models.BooleanField(default=False)
	desc=models.TextField()
	# episode_duration=models.DurationField(default=datetime.timedelta(microseconds=-1))

	def __str__(self):
		return self.episode_name

	class Meta:
		verbose_name_plural = "episode"