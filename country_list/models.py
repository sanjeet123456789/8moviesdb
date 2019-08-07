from django.db import models

class Country_list(models.Model):
	country_id=models.IntegerField()
	country_name=models.CharField(max_length=40)

	class Meta:
		verbose_name_plural='country_list'