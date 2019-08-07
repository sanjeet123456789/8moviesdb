from django.db import models

class Server_name(models.Model):
	server_name_id=models.IntegerField()
	server_name=models.CharField(max_length=40)



	class Meta:
		verbose_name_plural='server_name'