from django.db import models

# Create your models here.
class episode(models.Model):
	episode_id=models.PositiveSmallIntegerField(blank=False)
	episode_no=models.PositiveSmallIntegerField()
	episode_name=models.CharField(max_length=40)
	server_list_id=models.PositiveSmallIntegerField()
	views=models.PositiveIntegerField()
	type=models.PositiveSmallIntegerField()

	def __str__(self):
		return self.episode_name

	class Meta:
		verbose_name_plural = "episode"

