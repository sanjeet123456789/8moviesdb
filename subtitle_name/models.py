from django.db import models

class Subtitle_name(models.Model):
	subtitle_name_id=models.PositiveIntegerField()
	subtitle_name=models.CharField(max_length=40)
	subtitle_short_code=models.CharField(max_length=5)

	def __str__(self):
		return self.subtitle_name

	class Meta:
		verbose_name_plural="subtitle name"
