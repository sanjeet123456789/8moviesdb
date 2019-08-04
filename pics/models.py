from django.db import models

# Create your models here.
class pics(models.Model):
	image_id=models.CharField(max_length=50)
	pic_link=models.ImageField(upload_to='images/')

	def __str__(self):
		return self.image_id
	class Meta:
		verbose_name_plural="pics"

