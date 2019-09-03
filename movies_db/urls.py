"""movies_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies_list.views import movies_detail
from subtitle_name.views import about_me,subtitle_name_create,raw_subtite_name_create,updating_subtitle_name,delete_subtitle_name
from movies_list.main_view import movies_details
from users.views import register
from django.conf import settings
from django.conf.urls import url,include 
from django.conf.urls.static import static 
from pics.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',movies_detail,name="movies-detail"),
    path('about/',about_me,name="about-me"),
    path('register/',register,name="register"),
    path('subtitle_name_create/',subtitle_name_create,name="subtitle-name-create"),
	path('raw_subtitle_name_create/',raw_subtite_name_create,name="subtitle-name-create"),
    path('update_subtitle_name_create/',updating_subtitle_name,name="updating-subtitle-name"),
    path('subtitle_name/<int:id>/delete',delete_subtitle_name,name="delete-subtitle-name"),
    path('pal/',movies_detail,name="movies-detail"),
	path('image_upload', hotel_image_view, name = 'image-upload'), 
    path('success', success, name = 'success'), 
    path('movie/<int:movie_id>/',movies_details,name="movies-details"),
    path('movie_list/',include('movies_list.urls')),
    
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
