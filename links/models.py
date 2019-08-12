from django.db import models

# Create your models here.
class Link(models.Model):
	link_list_id=models.PositiveIntegerField()
	server_name_id=models.CharField(max_length=15)
	name=models.CharField(max_length=40)
	link=models.TextField()
	upvote=models.PositiveIntegerField()
	views=models.PositiveIntegerField()
	server_type_id=models.PositiveSmallIntegerField()
	subtitle_list_id=models.PositiveIntegerField()
	link_created_at=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.server_name

	class Meta:
		verbose_name_plural="link"
