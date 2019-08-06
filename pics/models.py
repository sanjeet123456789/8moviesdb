from django.db import models

class Pics(models.Model):
	image_id=models.IntegerField()
	pic_link=models.ImageField(upload_to='images/')

	class Meta:
		verbose_name_plural = "pics"