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

# class MyHandler(FileSystemEventHandler):

#     def on_any_event(self, event):
#         srcpath = event.src_path
#         print (srcpath, 'has been ',event.event_type)
#         print (datetime.datetime.now())
#         filename = srcpath[12:]
#         self.dropbox_fn(filename) # <----

#     def dropbox_fn(self, filename):  # <-----
#         print('In dropbox_fn:', filename)
class Handler():
	def get_movie_list(self,id):
		try:
			obj_movie_list=Movies_list.objects.get(id=id)
		except Movies_list.DoesNotExist:
			obj_movie_list=None 
		return obj_movie_list

	def get_award_list(self,award_id):
		try:
			obj_award_list=Award_list.objects.get(award_id=award_id)
		except Award_list.DoesNotExist:
			obj_award_list
		return obj_award_list

	def get_award_name(self,award_name_id):
		try:
			obj_award_name=Award_name.objects.get(award_name_id=award_name_id)
		except Award_name.DoesNotExist:
			obj_award_name=None
		return obj_award_name
	def get_cast(self,cast_id):
		try:
			obj_cast=Cast.objects.get(cast_id=cast_id)
		except Cast.DoesNotExist:
			obj_cast=None
		return obj_cast
	def get_country_list(self,country_id):
		try:
			obj_country_list=Country_list.objects.get(country_id=country_id)
		except Country_list.DoesNotExist:
			obj_country_list=None
		return obj_country_list
	def get_director(self,director_id):
		try:
			obj_director=Director.objects.get(director_id=director_id)
		except Director.DoesNotExist:
			obj_director=None
		return obj_director
	def get_season(self,season_id):
		try:
			obj_season=Season.objects.get(season_id=season_id)
		except Season.DoesNotExist:
			obj_season=None
		return obj_season
	def get_episode(self,episode_id):
		try:
			obj_episode=Episode.objects.get(episode_id=episode_id)
		except Episode.DoesNotExist:
			obj_episode=None
		return obj_episode
	def get_genre_list(self,genre_id):
		try:
			obj_genre_list=Genre_list.objects.get(genre_id=genres_id)
		except Genre_list.DoesNotExist:
			obj_genre_list=None
		return obj_genre_list
	def get_genre_name(self,genre_name_id):
		try:
			obj_genre_name=Genre_name.objects.get(genre_name_id=genre_name_id)
		except Genre_name.DoesNotExist:
			obj_genre_name=None
		return obj_genre_name
	def get_language_name(self,language_id):
		try:
			obj_language_name=Language_name.objects.get(language_id=language_id)
		except Language_name.DoesNotExist:
			obj_language_name=None
		return obj_language_name
	def get_link(self,link_list_id):
		try:
			obj_link=Link.objects.get(link_list_id=link_list_id)
		except Link.DoesNotExist:
			obj_link=None
		return obj_link
	def get_server_name(self,server_name_id):
		try:
			obj_server_name=Server_name.objects.get(server_name_id=server_name_id)
		except Server_name.DoesNotExist:
			obj_server_name=None
		return obj_server_name
	def get_server_type(self,server_type_id):
		try:
			obj_server_type=Server_type.objects.get(server_type_id=server_type_id)
		except Server_type.DoesNotExist:
			obj_server_type=None
		return obj_server_type
	def get_subtitle_list(self,subtitle_list_id):
		try:
			obj_subtitle_list=Subtitle_list.objects.get(subtitle_list_id=subtitle_list_id)
		except Subtitle_list.DoesNotExist:
			obj_subtitle_list=None
		return obj_subtitle_list
	def get_subtitle_name(self,subtitle_name_id):
		try:
			obj_subtitle_name=Subtitle_name.objects.get(subtitle_name_id=subtitle_name_id)
		except Subtitle_name.DoesNotExist:
			obj_subtitle_name=None
		return obj_subtitle_name
	def get_writer(self,writer_id):
		try:
			obj_writer=Writer.objects.get(writer_id=writer_id)
		except Writer.DoesNotExist:
			obj_writer=None
		return obj_writer
	def get_pics(self,image_id):
		try:
			obj_pics=Pics.objects.get(image_id=image_id)
		except Pics.DoesNotExist:
			obj_pics=None
		return obj_pics

	def get_all_movie_list(self,x):
		try:
			all_movie_list=Movies_list.objects.all()[:x]
		except Movie_list.DoesNotExist:
			all_movie_list=None
		return all_movie_list

class cards():
	def get_card_info(self,movies_id):
		handler=handler()
		obj_movie_list=handler.get_movie_list







def movies_details(request,movie_id):
	handler=Handler()
	obj_movie_list=handler.get_movie_list(id=movie_id)
	obj_award_list=handler.get_award_list(award_id=obj_movie_list.Awards_id)
	obj_award_name=handler.get_award_name(award_name_id=obj_award_list.award_name_id)
	obj_cast=Cast.objects.get(cast_id=obj_movie_list.cast_id)
	obj_country_list=handler.get_country_list(country_id=obj_movie_list.country_id)
	obj_director=handler.get_director(director_id=obj_movie_list.director_id)
	obj_season=handler.get_season(season_id=obj_movie_list.season_id)
	obj_episode=handler.get_episode(episode_id=obj_season.eposide_id)
	obj_genre_list=Genre_list.objects.get(genre_id=obj_movie_list.genres_list_id)
	obj_genre_name=Genre_name.objects.get(genre_name_id=obj_genre_list.genre_name_id)
	obj_language_name=handler.get_language_name(language_id=obj_movie_list.language_id)
	if obj_episode is not None:
		obj_link=handler.get_link(link_list_id=obj_episode.link_list_id)
	else:
		obj_link=None
	if obj_link is not  None:
		obj_server_name=handler.get_server_name(server_name_id=obj_link.server_name_id)
		obj_server_type=handler.get_server_type(server_type_id=obj_link.server_type_id)
		obj_subtitle_list=handler.get_subtitle_list(subtitle_list_id=obj_link.subtitle_list_id)
		
	else:
		obj_server_name=None
		obj_server_type=None
		obj_subtitle_list=None

	if obj_subtitle_list is not  None:
		obj_subtitle_name=handler.get_subtitle_name(subtitle_name_id=obj_subtitle_list.subtitle_name_id)
	else:	
		obj_subtitle_name=None

	
		
	
	obj_writer=handler.get_writer(writer_id=obj_movie_list.writer_id)
	
	
	obj_pics=handler.get_pics(image_id=obj_cast.image_id)
	
	
	
	# |obj_director.image_id|obj_writer.image_id



	tags=obj_movie_list.tags
	tags=tags.split(",")

	context={

		'movie_list':obj_movie_list,
		'award_list':obj_award_list,
		'award_name':obj_award_name,
		'cast':obj_cast,
		'country_list':obj_country_list,
		'director':obj_director,
		'season':obj_season,
		'episode':obj_episode,
		'genre_list':obj_genre_list,
		'genre_name':obj_genre_name,
		'language_name':obj_language_name,
		'link':obj_link,
		'server_name':obj_server_name,
		'server_type':obj_server_type,
		'subtitle_list':obj_subtitle_list,
		'subtitle_name':obj_subtitle_name,
		'writer':obj_writer,
		'pics':obj_pics,
		'tags':tags

	}
	return render(request,"movies_list_html/movie_post.html",context)


# Entry.objects.filter(name='name', title='title').exists()