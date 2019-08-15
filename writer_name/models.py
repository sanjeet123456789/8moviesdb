from django.db import models

class Writer_name(models.Model):
	writer_name_id=models.PositiveIntegerField(default=0)
	image_id=models.IntegerField(blank=False)


	class Meta:
		verbose_name_plural="writer name"
