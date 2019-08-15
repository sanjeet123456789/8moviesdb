from django.db import models

class Writer_name(models.Model):
	writer_name_id=models.PositiveIntegerField(default=0)
	writer_name=models.CharField(max_length=40)
	image_id=models.IntegerField(default=1)


	class Meta:
		verbose_name_plural="writer name"
