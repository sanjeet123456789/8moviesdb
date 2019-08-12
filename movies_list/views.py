from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Movies_list
from award_list.models import Award_list
from award_name.models import Award_name
from cast.models import Cast
from country_list.models import Country_list
from director.models import Director
from episode.models import Episode
from genre_list.models import Genre_list
from genre_name.models import Genre_name
from language_name.models import Language_name
from links.models import Link
from pics.models import Pics
from season.models import Season
from server_name.models import Server_name
from server_type.models import Server_type
from subtitle_list.models import Subtitle_list
from subtitle_name.models import Subtitle_name
from writer.models import Writer

def movies_detail(request):
	obj=Movies_list.objects.get(id=1)
	obj_language=Language_name.objects.get(language_id=obj.language_id)
	tags=obj.tags
	tags=tags.split(",")
	obj_cast=Cast.objects.get(cast_id=obj.cast_id)
	obj_pics=Pics.objects.get(image_id=obj_cast.image_id)
	obj_sesion=Season.objects.get(season_id=obj.season_id)



	



	context={
		'object':obj,
		'object1':obj_language,
		'tagw':tags,
		'cast_object':obj_cast.image_id,
		'image_object':obj_pics,
		'sesion_object':obj_sesion

	}
	return render(request,"movies_list_html/movies.html",context)



def index(request):
	return HttpResponse("Hello")


