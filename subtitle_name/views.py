from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Subtitle_name
from django.db.models import Max
r=Subtitle_name.objects.aggregate(Max('subtitle_name_id'))
x=[*r.values()]
print(x[0])
# from django.db.models import Max
# args = Subtitle_name.objects.filter(name='foo') # or whatever arbitrary queryset
# args.aggregate(Max('rating'))
# Create your views here.
from .forms import Subtitle_name_Form,Raw_Subtitle_name_Form,update_Subtitle_name_Form
def about_me(request,*args,**kargs):
	my_context={
	"my_text":"This is about us",
	"my_number":123
	}
	return render(request,"about.html",my_context)


def subtitle_name_create(request):
	form =Subtitle_name_Form(request.POST or None)
	if form.is_valid():
		form.save()
		# form.Subtitle_name_Form()
	context={
		'form':form
	}
	return render(request,"update_subtitle_name.html",context)


print(r)
def raw_subtite_name_create(request):
	my_form=Raw_Subtitle_name_Form()
	if request.method=="POST":
		my_form=Raw_Subtitle_name_Form(request.POST)
		if my_form.is_valid():
			# print(my_form.cleaned_data)
			print(request.POST["subtitle_name"])
			r=Subtitle_name.objects.aggregate(Max('subtitle_name_id'))
			x=[*r.values()]
			print(x[0])
		# 	Subtitle_name.objects.create(**my_form.cleaned_data)
			r=Subtitle_name(subtitle_name_id=x[0]+1,subtitle_name=request.POST["subtitle_name"],subtitle_short_code=request.POST["subtitle_short_code"])
			r.save()

		else:
			print(my_form.errors)
	context={
		"form":my_form
	}
	return render(request,"raw_update_subtitle_name.html",context)




def updating_subtitle_name(request):

	obj=get_object_or_404(Subtitle_name,pk=3)
	form=update_Subtitle_name_Form(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
	context={
		"form":form,
		"subtitle_name_id":f"Update{obj.subtitle_name_id}"
		}
	return render(request,'update_subtitle_name.html',context)

def delete_subtitle_name(request,id):
	obj=get_object_or_404(Subtitle_name,subtitle_name_id=id)
	if request.method=="POST":
		print("yes motherfucker")
		obj.delete()
	print(obj.subtitle_name)
	context={
		"obj":obj
	}
	return render(request,"delete_subtitle_name.html",context)