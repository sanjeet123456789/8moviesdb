from django.db import models

class Language_name(models.Model):
	language_id=models.IntegerField()
	language_name=models.CharField(max_length=40)
	language_short_code=models.TextField(max_length=5)



	def __str__(self):
		return self.language_name

	class Meta:
		verbose_name_plural="language_name"
