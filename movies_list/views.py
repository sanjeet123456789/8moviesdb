from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import movies_list

def movies_detail(request):
	obj=movies_list.objects.get(id=1)
	context={
		'object':obj
	}
	return render(request,"movies_list_html/movies.html",context)



def index(request):
	return HttpResponse("Hello")


