from django.db import models

# Create your models here.
class Cast(models.Model):
	cast_id=models.IntegerField()
	cast_no=models.IntegerField()
	cast_name_id=models.PositiveIntegerField(default=0)
	role=models.CharField(max_length=40,blank=False)



	class Meta:
		verbose_name_plural = "cast"