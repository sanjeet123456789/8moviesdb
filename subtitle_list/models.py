from django.db import models

# Create your models here.
class Subtitle_list(models.Model):
	subtitle_list_id=models.PositiveIntegerField()
	subtitle_no=models.PositiveIntegerField()
	subtitle_name_id=models.PositiveIntegerField()

	def __str__(self):
		return self.subtitle_list_id

	class Meta:
		verbose_name_plural="subtitle list"