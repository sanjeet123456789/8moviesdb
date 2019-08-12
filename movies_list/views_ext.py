
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .main_view import *





# def movies_details(request,movie_id):
# 	obj=Movies_list.objects.get(id=movie_id)
# 	obj_language=Language_name.objects.get(language_id=obj.language_id)
# 	tags=obj.tags
# 	tags=tags.split(",")
# 	obj_cast=Cast.objects.get(cast_id=obj.cast_id)
# 	obj_pics=Pics.objects.get(image_id=obj_cast.image_id)
# 	obj_sesion=Season.objects.get(season_id=obj.season_id)


# 	context={
# 		'object':obj,
# 		'object1':obj_language,
# 		'tagw':tags,
# 		'cast_object':obj_cast.image_id,
# 		'image_object':obj_pics,
# 		'sesion_object':obj_sesion
# 	}
# 	return render(request,"movies_list_html/movie_post.html",context)






def movies_list(request):
	movie_list=Movies_list.objects.all()[:10]
	context={
		'movie_list':movie_list

	}
	return render(request,'movies_list_html/movie_list.html',context)


