from django.db import models

# Create your models here.

class pics(models.Model):
	image_id=models.SmallIntegerField()
	pic_link=models.FilePathField(path=None, match=None, recursive=False, max_length=100)

