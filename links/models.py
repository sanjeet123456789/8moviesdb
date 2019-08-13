from django.db import models

# Create your models here.
class Link(models.Model):
	link_list_id=models.PositiveIntegerField()
	server_name_id=models.CharField(max_length=15)
	name=models.CharField(max_length=40)
	link=models.TextField()
	upvote=models.PositiveIntegerField(default=0)
	views=models.PositiveIntegerField(default=0)
	server_type_id=models.PositiveSmallIntegerField(default=1)
	subtitle_list_id=models.PositiveIntegerField(default=1)
	link_created_at=models.DateTimeField(auto_now=True, auto_now_add=False)
	quality_id=models.PositiveIntegerField(default=1)


	class Meta:
		verbose_name_plural="link"
