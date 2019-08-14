from django.db import models

class Quality_name(models.Model):
	quality_name_id=models.PositiveIntegerField()
	quality_name=models.CharField(max_length=40)
	priority=models.PositiveIntegerField()


	class Meta:
		verbose_name_plural="quality name"
