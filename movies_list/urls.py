from django.conf.urls import url
from . import views_ext


urlpatterns=[
	url(r'^$',views_ext.movies_list,name='movies_listing')


]