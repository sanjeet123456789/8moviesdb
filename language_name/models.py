from django.db import models

class Language_name(models.Model):
	language_id=models.PositiveSmallIntegerField()
	language_name=models.CharField(max_length=40)



	def __str__(self):
		return self.language_name

	class Meta:
		verbose_name_plural="language_name"
