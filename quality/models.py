from django.db import models

class Quality(models.Model):
	quality_id=models.PositiveIntegerField()
	quality_name=models.CharField(max_length=40)
	quality_short_name=models.CharField(max_length=6)
	quality_priority=models.PositiveIntegerField()
	
