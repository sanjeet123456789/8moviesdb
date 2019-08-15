from django.db import models

# Create your models here.
class Writer(models.Model):
	writer_id=models.IntegerField()
	writer_name_id=models.PositiveIntegerField(default=0)
	image_id=models.PositiveSmallIntegerField()


	class Meta:
		verbose_name_plural="writer"