from django.db import models

class Award_list(models.Model):
	award_id=models.IntegerField()
	award_name_id=models.PositiveSmallIntegerField()
	
	def __str__(self):
		return self.award_id
	class Meta:
		verbose_name_plural="award_list" 
