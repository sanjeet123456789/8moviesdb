from django.db import models

class Quality(models.Model):
	quality_id=models.PositiveIntegerField()
	quality_name_id=models.PositiveIntegerField()
	class Meta:
		verbose_name_plural='quality'

