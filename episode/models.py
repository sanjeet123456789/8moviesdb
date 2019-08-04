from django.db import models

# Create your models here.
class episode(models.model):
	id=models.AutoField()
	episode_id=models.PositiveSmallIntegerField(max_length=5,blank=False)
	episode_no=models.PositiveSmallIntegerField(max_length=5)
	server_list_id=models.PositiveSmallIntegerField(max_length=5)
	views=models.PositiveIntegerField()
	type=models.PositiveSmallIntegerField(max_length=3)

