
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
	handler=Handler()
	movie_list=handler.get_all_movie_list(10)
	context={
		'movie_list':movie_list

	}
	return render(request,'movies_list_html/movie_list.html',context)




# def create_movies_list(request):
# 	my_form=Movies_list_form()
# 	if request.method=="POST":
# 		my_form=Movies_list_form(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			Indian_movies.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context={
# 		"form":my_form
# 	}
# 	return render(request,"prodiuuct/completeform.html",context)


