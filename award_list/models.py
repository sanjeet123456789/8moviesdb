from django.db import models

class Award_list(models.Model):
	award_id=models.IntegerField()
	award_no=models.PositiveSmallIntegerField()
	award_name_id=models.PositiveSmallIntegerField()

	class Meta:
		verbose_name_plural="award_list" 
