from django.db import models

class Server_type(models.Model):
	server_type_id=models.IntegerField()
	server_type=models.CharField(max_length=40)


	class Meta:
		verbose_name_plural='server_type'
