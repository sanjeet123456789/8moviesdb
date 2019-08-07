from django.db import models

# Create your models here.
class Episode(models.Model):
	episode_id=models.IntegerField(blank=False)
	episode_no=models.IntegerField()
	episode_name=models.CharField(max_length=40)
	server_list_id=models.IntegerField()
	views=models.IntegerField()

	def __str__(self):
		return self.episode_name

	class Meta:
		verbose_name_plural = "episode"

