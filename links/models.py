from django.db import models

# Create your models here.
class Link(models.Model):
	server_list_id=models.PositiveIntegerField()
	server_name_id=models.CharField(max_length=15)
	link=models.TextField()
	upvote=models.PositiveIntegerField()
	views=models.PositiveIntegerField()
	server_type_id=models.PositiveSmallIntegerField()
	subtitle=models.BooleanField()
	def __str__(self):
		return self.server_name

	class Meta:
		verbose_name_plural="link"
