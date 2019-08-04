from django.db import models

class Award_name(models.Model):
	award_name_id=models.PositiveSmallIntegerField()
	award_name=models.CharField(max_length=40,blank=False)

	def __str__(self):
		return selfaward_name
	class Meta:
		verbose_name_plural= "award_name"