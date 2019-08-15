from django.db import models

# Create your models here.
class Cast_name(models.Model):
	cast_name_id=models.PositiveIntegerField(default=1)
	cast_name=models.CharField(max_length=40)
	image_id=models.IntegerField(default=None)


	class Meta:
		verbose_name_plural="cast_name"