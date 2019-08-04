from django.db import models

# Create your models here.
class Cast(models.Model):
	cast_id=models.PositiveSmallIntegerField()
	cast_name=models.CharField(max_length=40,blank=False)
	actual_name=models.CharField(max_length=40,blank=False)
	role=models.CharField(max_length=40,blank=False)
	image_id=models.PositiveSmallIntegerField(blank=False)
	def __str__(self):
		return self.cast_name

	class Meta:
		verbose_name_plural = "cast"