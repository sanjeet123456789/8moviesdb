from django.conf.urls import url
from . import views_ext,main_view


urlpatterns=[
	url(r'^$',views_ext.movies_list,name='movies_listing')


]