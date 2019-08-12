from django.db import models

# Create your models here.
class Episode(models.Model):
	episode_id=models.IntegerField(blank=False)
	episode_no=models.IntegerField()
	episode_name=models.CharField(max_length=40)
	link_list_id=models.IntegerField()

	views=models.IntegerField()
	adult=models.BooleanField()
	filler=models.BooleanField()
	desc=models.TextField()

	def __str__(self):
		return self.episode_name

	class Meta:
		verbose_name_plural = "episode"

