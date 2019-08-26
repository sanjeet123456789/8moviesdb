python manage.py shell

from movies_list.models import Movies_list
from award_list.models import Award_list
from award_name.models import Award_name
from cast.models import Cast
from cast_name.models import Cast_name
from country_list.models import Country_list
from director.models import Director
from director_name.models import Director_name
from episode.models import Episode
from genre_list.models import Genre_list
from genre_name.models import Genre_name
from language_name.models import Language_name
from links.models import Link
from pics.models import Pics
from quality.models import Quality
from season.models import Season
from server_name.models import Server_name
from server_type.models import Server_type
from subtitle_list.models import Subtitle_list
from subtitle_name.models import Subtitle_name
from writer.models import Writer
from writer_name.models import Writer_name












from country_list.models import Country_list
c=Country_list(country_id=1,country_name="United States")
c.save()
c=Country_list(country_id=2,country_name="United Kingdom")
c.save()
c=Country_list(country_id=3,country_name="Canada")
c.save()
c=Country_list(country_id=4,country_name="France")
c.save()
c=Country_list(country_id=5,country_name="Germany")
c.save()
c=Country_list(country_id=6,country_name="Japan")
c.save()
c=Country_list(country_id=7,country_name="Australia")
c.save()
c=Country_list(country_id=8,country_name="Italy")
c.save()
c=Country_list(country_id=9,country_name="International")
c.save()
c=Country_list(country_id=10,country_name="Spain")
c.save()
c=Country_list(country_id=11,country_name="Hong-Kong")
c.save()
c=Country_list(country_id=12,country_name="China")
c.save()
c=Country_list(country_id=13,country_name="Ireland")
c.save()
c=Country_list(country_id=14,country_name="Korea")
c.save()
c=Country_list(country_id=15,country_name="India")
c.save()
c=Country_list(country_id=16,country_name="Belgium")
c.save()
c=Country_list(country_id=17,country_name="Denmark")
c.save()
c=Country_list(country_id=18,country_name="Sweden")
c.save()
c=Country_list(country_id=19,country_name="New-Zealand")
c.save()
c=Country_list(country_id=20,country_name="Netherlands")
c.save()
c=Country_list(country_id=21,country_name="South Africa")
c.save()
c=Country_list(country_id=22,country_name="Norway")
c.save()
c=Country_list(country_id=23,country_name="Mexico")
c.save()
c=Country_list(country_id=24,country_name="Switzerland")
c.save()
c=Country_list(country_id=25,country_name="Australia")
c.save()
c=Country_list(country_id=26,country_name="Czech Republic")
c.save()
c=Country_list(country_id=27,country_name="Brazil")
c.save()
c=Country_list(country_id=28,country_name="Russia")
c.save()
c=Country_list(country_id=29,country_name="Argentina")
c.save()
c=Country_list(country_id=30,country_name="Hungary")
c.save()
c=Country_list(country_id=31,country_name="Poland")
c.save()
c=Country_list(country_id=32,country_name="Finland")
c.save()
c=Country_list(country_id=33,country_name="Israel")
c.save()
c=Country_list(country_id=34,country_name="Romania")
c.save()
c=Country_list(country_id=35,country_name="Luxemberg")
c.save()
c=Country_list(country_id=36,country_name="Thailand")
c.save()
c=Country_list(country_id=37,country_name="Taiwan")
c.save()





from genre_name.models import Genre_name
g=Genre_name(genre_name_id=1,genre_name="Action")
g.save()
g=Genre_name(genre_name_id=2,genre_name="Adventure")
g.save()
g=Genre_name(genre_name_id=3,genre_name="Animation")
g.save()
g=Genre_name(genre_name_id=4,genre_name="Biography")
g.save()
g=Genre_name(genre_name_id=5,genre_name="Costume")
g.save()
g=Genre_name(genre_name_id=6,genre_name="Comedy")
g.save()
g=Genre_name(genre_name_id=7,genre_name="Crime")
g.save()
g=Genre_name(genre_name_id=8,genre_name="Documentary")
g.save()
g=Genre_name(genre_name_id=9,genre_name="Drama")
g.save()
g=Genre_name(genre_name_id=10,genre_name="Family")
g.save()
g=Genre_name(genre_name_id=11,genre_name="Fantasy")
g.save()
g=Genre_name(genre_name_id=12,genre_name="Game-show")
g.save()
g=Genre_name(genre_name_id=13,genre_name="History")
g.save()
g=Genre_name(genre_name_id=14,genre_name="Horrer")
g.save()
g=Genre_name(genre_name_id=15,genre_name="Kungfu")
g.save()
g=Genre_name(genre_name_id=16,genre_name="Music")
g.save()
g=Genre_name(genre_name_id=17,genre_name="Mystery")
g.save()
g=Genre_name(genre_name_id=18,genre_name="Reality-TV")
g.save()
g=Genre_name(genre_name_id=19,genre_name="Romance")
g.save()
g=Genre_name(genre_name_id=20,genre_name="Sci-fi")
g.save()
g=Genre_name(genre_name_id=21,genre_name="Sport")
g.save()
g=Genre_name(genre_name_id=22,genre_name="Thriller")
g.save()
g=Genre_name(genre_name_id=23,genre_name="Tv-show")
g.save()
g=Genre_name(genre_name_id=24,genre_name="war")
g.save()
g=Genre_name(genre_name_id=25,genre_name="Western")
g.save()





from language_name.models import Language_name
p=Language_name(language_id=11,language_name="Afrikaans",language_short_code="af")
p.save()
p=Language_name(language_id=12,language_name="Albanian",language_short_code="sq")
p.save()
p=Language_name(language_id=13,language_name="Arabic",language_short_code="ar")
p.save()
p=Language_name(language_id=14,language_name="Azerbaijani",language_short_code="eu")
p.save()
p=Language_name(language_id=15,language_name="Basque",language_short_code="EN")
p.save()
p=Language_name(language_id=16,language_name="Bengali",language_short_code="bn")
p.save()
p=Language_name(language_id=17,language_name="Belarusian",language_short_code="be")
p.save()
p=Language_name(language_id=18,language_name="Catalan",language_short_code="ca")
p.save()
p=Language_name(language_id=19,language_name="Chinese Simplified",language_short_code="zh-CN")
p.save()
p=Language_name(language_id=20,language_name="Chinese Traditional",language_short_code="zh-TW")
p.save()
p=Language_name(language_id=21,language_name="Croatian",language_short_code="hr")
p.save()
p=Language_name(language_id=22,language_name="Czech",language_short_code="cs")
p.save()
p=Language_name(language_id=23,language_name="Danish",language_short_code="da")
p.save()
p=Language_name(language_id=24,language_name="Dutch",language_short_code="nl")
p.save()
p=Language_name(language_id=25,language_name="English",language_short_code="en")
p.save()
p=Language_name(language_id=26,language_name="Estonian",language_short_code="et")
p.save()
p=Language_name(language_id=27,language_name="Filipino",language_short_code="tl")
p.save()
p=Language_name(language_id=28,language_name="Finnish",language_short_code="fi")
p.save()
p=Language_name(language_id=29,language_name="French",language_short_code="fr")
p.save()
p=Language_name(language_id=30,language_name="Galician",language_short_code="gl")
p.save()
p=Language_name(language_id=31,language_name="Georgian",language_short_code="ka")
p.save()
p=Language_name(language_id=32,language_name="Greek",language_short_code="el")
p.save()
p=Language_name(language_id=33,language_name="Gujarati",language_short_code="gu")
p.save()
p=Language_name(language_id=34,language_name="Haitian Creole",language_short_code="ht")
p.save()
p=Language_name(language_id=35,language_name="Hindi",language_short_code="hi")
p.save()
p=Language_name(language_id=36,language_name="Hungarian",language_short_code="hu")
p.save()
p=Language_name(language_id=37,language_name="Icelandic",language_short_code="is")
p.save()
p=Language_name(language_id=38,language_name="Indonesian",language_short_code="id")
p.save()
p=Language_name(language_id=39,language_name="Irish",language_short_code="ga")
p.save()
p=Language_name(language_id=40,language_name="Italian",language_short_code="it")
p.save()
p=Language_name(language_id=41,language_name="Japanese",language_short_code="ja")
p.save()
p=Language_name(language_id=42,language_name="Kannada",language_short_code="kn")
p.save()
p=Language_name(language_id=43,language_name="Korean",language_short_code="ko")
p.save()
p=Language_name(language_id=44,language_name="Latin",language_short_code="la")
p.save()
p=Language_name(language_id=45,language_name="Latvian",language_short_code="lv")
p.save()
p=Language_name(language_id=46,language_name="Lithuanian",language_short_code="lt")
p.save()
p=Language_name(language_id=47,language_name="Macedonian",language_short_code="mk")
p.save()
p=Language_name(language_id=48,language_name="Malay",language_short_code="ms")
p.save()
p=Language_name(language_id=49,language_name="Maltese",language_short_code="mt")
p.save()
p=Language_name(language_id=50,language_name="Norwegian",language_short_code="no")
p.save()
p=Language_name(language_id=51,language_name="Persian",language_short_code="fa")
p.save()
p=Language_name(language_id=52,language_name="Polish",language_short_code="pl")
p.save()
p=Language_name(language_id=53,language_name="Portuguese",language_short_code="pt")
p.save()
p=Language_name(language_id=54,language_name="Romanian",language_short_code="ro")
p.save()
p=Language_name(language_id=55,language_name="Russian",language_short_code="ru")
p.save()
p=Language_name(language_id=56,language_name="Serbian",language_short_code="sr")
p.save()
p=Language_name(language_id=57,language_name="Slovak",language_short_code="sk")
p.save()
p=Language_name(language_id=58,language_name="Slovenian",language_short_code="sl")
p.save()
p=Language_name(language_id=59,language_name="Spanish",language_short_code="es")
p.save()
p=Language_name(language_id=60,language_name="Swahili",language_short_code="sw")
p.save()
p=Language_name(language_id=61,language_name="Swedish",language_short_code="sv")
p.save()
p=Language_name(language_id=62,language_name="Tamil",language_short_code="ta")
p.save()
p=Language_name(language_id=63,language_name="Telugu",language_short_code="te")
p.save()
p=Language_name(language_id=64,language_name="Thai",language_short_code="th")
p.save()
p=Language_name(language_id=65,language_name="Turkish",language_short_code="tr")
p.save()
p=Language_name(language_id=66,language_name="Ukrainian",language_short_code="uk")
p.save()
p=Language_name(language_id=67,language_name="Urdu",language_short_code="ur")
p.save()
p=Language_name(language_id=68,language_name="Vietnamese",language_short_code="vi")
p.save()
p=Language_name(language_id=69,language_name="Welsh",language_short_code="cy")
p.save()
p=Language_name(language_id=70,language_name="Yiddish",language_short_code="yi")
p.save()





from quality_name.models import Quality_name
q=Quality_name(quality_name_id=1,quality_name="CAM",priority=1)
q.save()
q=Quality_name(quality_name_id=2,quality_name="144p",priority=2)
q.save()
q=Quality_name(quality_name_id=3,quality_name="240p",priority=3)
q.save()
q=Quality_name(quality_name_id=4,quality_name="360p",priority=4)
q.save()
q=Quality_name(quality_name_id=5,quality_name="480p",priority=5)
q.save()
q=Quality_name(quality_name_id=6,quality_name="720pᴴᴰ",priority=6)
q.save()
q=Quality_name(quality_name_id=7,quality_name="1080pᴴᴰ",priority=7)
q.save()
q=Quality_name(quality_name_id=8,quality_name="1440pᴴᴰ",priority=8)
q.save()
q=Quality_name(quality_name_id=9,quality_name="2160p⁴ᴷ",priority=9)
q.save()
q=Quality_name(quality_name_id=10,quality_name="4320p⁸ᴷ",priority=10)
q.save()



from subtitle_name.models import Subtitle_name
sub=Subtitle_name(subtitle_name_id=11,subtitle_name="Afrikaans",subtitle_short_code="af")
sub.save()
sub=Subtitle_name(subtitle_name_id=12,subtitle_name="Albanian",subtitle_short_code="sq")
sub.save()
sub=Subtitle_name(subtitle_name_id=13,subtitle_name="Arabic",subtitle_short_code="ar")
sub.save()
sub=Subtitle_name(subtitle_name_id=14,subtitle_name="Azerbaijani",subtitle_short_code="eu")
sub.save()
sub=Subtitle_name(subtitle_name_id=15,subtitle_name="Basque",subtitle_short_code="EN")
sub.save()
sub=Subtitle_name(subtitle_name_id=16,subtitle_name="Bengali",subtitle_short_code="bn")
sub.save()
sub=Subtitle_name(subtitle_name_id=17,subtitle_name="Belarusian",subtitle_short_code="be")
sub.save()
sub=Subtitle_name(subtitle_name_id=18,subtitle_name="Catalan",subtitle_short_code="ca")
sub.save()
sub=Subtitle_name(subtitle_name_id=19,subtitle_name="Chinese Simsublified",subtitle_short_code="zh-CN")
sub.save()
sub=Subtitle_name(subtitle_name_id=20,subtitle_name="Chinese Traditional",subtitle_short_code="zh-TW")
sub.save()
sub=Subtitle_name(subtitle_name_id=21,subtitle_name="Croatian",subtitle_short_code="hr")
sub.save()
sub=Subtitle_name(subtitle_name_id=22,subtitle_name="Czech",subtitle_short_code="cs")
sub.save()
sub=Subtitle_name(subtitle_name_id=23,subtitle_name="Danish",subtitle_short_code="da")
sub.save()
sub=Subtitle_name(subtitle_name_id=24,subtitle_name="Dutch",subtitle_short_code="nl")
sub.save()
sub=Subtitle_name(subtitle_name_id=25,subtitle_name="English",subtitle_short_code="en")
sub.save()
sub=Subtitle_name(subtitle_name_id=26,subtitle_name="Estonian",subtitle_short_code="et")
sub.save()
sub=Subtitle_name(subtitle_name_id=27,subtitle_name="Filisubino",subtitle_short_code="tl")
sub.save()
sub=Subtitle_name(subtitle_name_id=28,subtitle_name="Finnish",subtitle_short_code="fi")
sub.save()
sub=Subtitle_name(subtitle_name_id=29,subtitle_name="French",subtitle_short_code="fr")
sub.save()
sub=Subtitle_name(subtitle_name_id=30,subtitle_name="Galician",subtitle_short_code="gl")
sub.save()
sub=Subtitle_name(subtitle_name_id=31,subtitle_name="Georgian",subtitle_short_code="ka")
sub.save()
sub=Subtitle_name(subtitle_name_id=32,subtitle_name="Greek",subtitle_short_code="el")
sub.save()
sub=Subtitle_name(subtitle_name_id=33,subtitle_name="Gujarati",subtitle_short_code="gu")
sub.save()
sub=Subtitle_name(subtitle_name_id=34,subtitle_name="Haitian Creole",subtitle_short_code="ht")
sub.save()
sub=Subtitle_name(subtitle_name_id=35,subtitle_name="Hindi",subtitle_short_code="hi")
sub.save()
sub=Subtitle_name(subtitle_name_id=36,subtitle_name="Hungarian",subtitle_short_code="hu")
sub.save()
sub=Subtitle_name(subtitle_name_id=37,subtitle_name="Icelandic",subtitle_short_code="is")
sub.save()
sub=Subtitle_name(subtitle_name_id=38,subtitle_name="Indonesian",subtitle_short_code="id")
sub.save()
sub=Subtitle_name(subtitle_name_id=39,subtitle_name="Irish",subtitle_short_code="ga")
sub.save()
sub=Subtitle_name(subtitle_name_id=40,subtitle_name="Italian",subtitle_short_code="it")
sub.save()
sub=Subtitle_name(subtitle_name_id=41,subtitle_name="Jasubanese",subtitle_short_code="ja")
sub.save()
sub=Subtitle_name(subtitle_name_id=42,subtitle_name="Kannada",subtitle_short_code="kn")
sub.save()
sub=Subtitle_name(subtitle_name_id=43,subtitle_name="Korean",subtitle_short_code="ko")
sub.save()
sub=Subtitle_name(subtitle_name_id=44,subtitle_name="Latin",subtitle_short_code="la")
sub.save()
sub=Subtitle_name(subtitle_name_id=45,subtitle_name="Latvian",subtitle_short_code="lv")
sub.save()
sub=Subtitle_name(subtitle_name_id=46,subtitle_name="Lithuanian",subtitle_short_code="lt")
sub.save()
sub=Subtitle_name(subtitle_name_id=47,subtitle_name="Macedonian",subtitle_short_code="mk")
sub.save()
sub=Subtitle_name(subtitle_name_id=48,subtitle_name="Malay",subtitle_short_code="ms")
sub.save()
sub=Subtitle_name(subtitle_name_id=49,subtitle_name="Maltese",subtitle_short_code="mt")
sub.save()
sub=Subtitle_name(subtitle_name_id=50,subtitle_name="Norwegian",subtitle_short_code="no")
sub.save()
sub=Subtitle_name(subtitle_name_id=51,subtitle_name="Persian",subtitle_short_code="fa")
sub.save()
sub=Subtitle_name(subtitle_name_id=52,subtitle_name="Polish",subtitle_short_code="subl")
sub.save()
sub=Subtitle_name(subtitle_name_id=53,subtitle_name="Portuguese",subtitle_short_code="subt")
sub.save()
sub=Subtitle_name(subtitle_name_id=54,subtitle_name="Romanian",subtitle_short_code="ro")
sub.save()
sub=Subtitle_name(subtitle_name_id=55,subtitle_name="Russian",subtitle_short_code="ru")
sub.save()
sub=Subtitle_name(subtitle_name_id=56,subtitle_name="Serbian",subtitle_short_code="sr")
sub.save()
sub=Subtitle_name(subtitle_name_id=57,subtitle_name="Slovak",subtitle_short_code="sk")
sub.save()
sub=Subtitle_name(subtitle_name_id=58,subtitle_name="Slovenian",subtitle_short_code="sl")
sub.save()
sub=Subtitle_name(subtitle_name_id=59,subtitle_name="Ssubanish",subtitle_short_code="es")
sub.save()
sub=Subtitle_name(subtitle_name_id=60,subtitle_name="Swahili",subtitle_short_code="sw")
sub.save()
sub=Subtitle_name(subtitle_name_id=61,subtitle_name="Swedish",subtitle_short_code="sv")
sub.save()
sub=Subtitle_name(subtitle_name_id=62,subtitle_name="Tamil",subtitle_short_code="ta")
sub.save()
sub=Subtitle_name(subtitle_name_id=63,subtitle_name="Telugu",subtitle_short_code="te")
sub.save()
sub=Subtitle_name(subtitle_name_id=64,subtitle_name="Thai",subtitle_short_code="th")
sub.save()
sub=Subtitle_name(subtitle_name_id=65,subtitle_name="Turkish",subtitle_short_code="tr")
sub.save()
sub=Subtitle_name(subtitle_name_id=66,subtitle_name="Ukrainian",subtitle_short_code="uk")
sub.save()
sub=Subtitle_name(subtitle_name_id=67,subtitle_name="Urdu",subtitle_short_code="ur")
sub.save()
sub=Subtitle_name(subtitle_name_id=68,subtitle_name="Vietnamese",subtitle_short_code="vi")
sub.save()
sub=Subtitle_name(subtitle_name_id=69,subtitle_name="Welsh",subtitle_short_code="cy")
sub.save()
sub=Subtitle_name(subtitle_name_id=70,subtitle_name="Yiddish",subtitle_short_code="yi")
sub.save()







































from movies_list.models import Movies_list
movies=Movies_list(id=2,name="Fast & FUrious Presents:Hobbs &shaw",genre_list_id=2,cast_id=2,director_id=2,writer_id=2,country_id=1,story_line="Lawmen Luke Hobbs and outcast Deckard shaw from and unlikel;y allience when cyber genetically enterance willian threten the future of humanity",season_id=2,cost=120000,award_id=2,release='2019-07-31',created_at='2019-08-15',language_id=25,imdb_ratting=6.3,trailer_link="https://youtube.com/",views=1262,likes=500,ratting=2.6,imdb_link="https://www.imdb.com/title/tt6806448/",tags="fast,furious,hobbs,&shaw")
movies.save()
genre_list=Genre_list(genre_id=2,genre_no=1,genre_name_id=2)
genre_list.save()
genre_list=Genre_list(genre_id=2,genre_no=2,genre_name_id=1)
genre_list.save()
cast=Cast(cast_id=2,cast_no=1,cast_name_id=1,role="actor")
cast.save()
cast=Cast(cast_id=2,cast_no=2,cast_name_id=2,role="actor")
cast.save()
cast=Cast(cast_id=2,cast_no=3,cast_name_id=3,role="actor")
cast.save()
cast=Cast(cast_id=2,cast_no=4,cast_name_id=4,role="actor")
cast.save()
cast_nam=Cast_name(cast_name_id=1,cast_name="Dwayne Johnson",image_id=1)
cast_nam.save()
cast_nam=Cast_name(cast_name_id=2,cast_name="Idris Elba",image_id=2)
cast_nam.save()
cast_nam=Cast_name(cast_name_id=3,cast_name="Vanessa",image_id=3)
cast_nam.save()
cast_nam=Cast_name(cast_name_id=4,cast_name="Jason Stathan",image_id=4)
cast_nam.save()
director=Director(director_id=2,director_no=1,director_name_id=1)
director.save()
director_name=Director_name(director_name_id=1,director_name="David Leitch",image_id=5)
director_name.save()
season=Season(season_id=2,season_no=1,season_name='1',episode_id=2,plot="This is plot section of season")
season.save()
episode=Episode(episode_id=2,episode_no=1,episode_name="EP 1",link_list_id=2,desc="this is episode description")
episode.save()





link=Link(link_list_id=2,name="ep1 link1",link="https://youtube.com/",subtitle_list_id=2,quality_id=2)
link.save()
server_name=Server_name(server_name_id=1,server_name="openload")
server_name.save()
server_type=Server_type(server_type_id=1,server_type="download")
server_type.save()
subtitle_list=Subtitle_list(subtitle_list_id=2,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
quality=Quality(quality_id=2,quality_name_id=2)
quality.save()
writer=Writer(writer_id=2,writer_name_id=3)
writer.save()
writer_name=Writer_name(writer_name_id=3,writer_name="kalia")
writer_name.save()




movies=Movies_list(id=5,name="Game of Thrones",genre_list_id=5,cast_id=5,director_id=5,writer_id=5,country_id=1,story_line="Tn the mythical continent of west error several powerful familier for control of the seven Kingdom",season_id=5,cost=40000,award_id=5,release='2019-04-14',imdb_ratting=9.1,trailer_link="https://youtube.com/",ratting=8.1,imdb_link="https://imdb.com.movies/12421",tags="games,of,Thrones,season-1,2,3,4,5,6")
movies.save()
genre_list=Genre_list(genre_id=5,genre_no=1,genre_name_id=9)
genre_list.save()
genre_list=Genre_list(genre_id=5,genre_no=2,genre_name_id=2)
genre_list.save()
genre_list=Genre_list(genre_id=5,genre_no=3,genre_name_id=19)
genre_list.save()
genre_list=Genre_list(genre_id=5,genre_no=4,genre_name_id=1)
genre_list.save()
genre_list=Genre_list(genre_id=5,genre_no=5,genre_name_id=11)
genre_list.save()
cast=Cast(cast_id=5,cast_no=1,cast_name_id=5,role="actor")
cast.save()
cast=Cast(cast_id=5,cast_no=2,cast_name_id=6,role="actor")
cast.save()
cast=Cast(cast_id=5,cast_no=3,cast_name_id=7,role="actor")
cast.save()
cast=Cast(cast_id=5,cast_no=4,cast_name_id=8,role="actor")
cast.save()
cast_name=Cast_name(cast_name_id=5,cast_name="Lena Headey",image_id=1)
cast_name.save()
cast_name=Cast_name(cast_name_id=6,cast_name="Peter Dinklag ",image_id=12)
cast_name.save()
cast_name=Cast_name(cast_name_id=7,cast_name="Kit Harington",image_id=10)
cast_name.save()
cast_name=Cast_name(cast_name_id=8,cast_name="Emilia Clark",image_id=11)
cast_name.save()
director=Director(director_id=5,director_no=1,director_name_id=2)
director.save()
director_name=Director_name(director_name_id=2,director_name="peter Pan",image_id=12)
director_name.save()


season=Season(season_id=5,season_no=1,season_name='Game of Throne Season - 1',episode_id=15,plot="This is plot section of game of throne seaso 1")
season.save()
episode=Episode(episode_id=15,episode_no=1,episode_name="Episode 1",link_list_id=15,desc="this is episode 1 description")
episode.save()
episode=Episode(episode_id=15,episode_no=2,episode_name="Episode 2",link_list_id=16,desc="this is episode 2 description")
episode.save()
episode=Episode(episode_id=15,episode_no=3,episode_name="Episode 3",link_list_id=17,desc="this is episode 3 description")
episode.save()
episode=Episode(episode_id=15,episode_no=4,episode_name="Episode 4",link_list_id=18,desc="this is episode 4 description")
episode.save()
episode=Episode(episode_id=15,episode_no=5,episode_name="Episode 5",link_list_id=19,desc="this is episode 5 description")
episode.save()

season=Season(season_id=5,season_no=2,season_name='Game of Throne Season - 2',episode_id=16,plot="This is plot section of game of throne season 2")
season.save()
episode=Episode(episode_id=16,episode_no=1,episode_name="Episode 2.1",link_list_id=20,desc="this is episode 2.1 description")
episode.save()
episode=Episode(episode_id=16,episode_no=2,episode_name="Episode 2.2",link_list_id=21,desc="this is episode 2.2 description")
episode.save()
episode=Episode(episode_id=16,episode_no=3,episode_name="Episode 2.3",link_list_id=22,desc="this is episode 2.3 description")
episode.save()
episode=Episode(episode_id=16,episode_no=4,episode_name="Episode 2.4",link_list_id=23,desc="this is episode 2.4 description")
episode.save()
episode=Episode(episode_id=16,episode_no=5,episode_name="Episode 2.5",link_list_id=24,desc="this is episode 2.5 description")
episode.save()

season=Season(season_id=5,season_no=3,season_name='Game of Throne Season - 3',episode_id=17,plot="This is plot section of game of throne season 3")
season.save()
episode=Episode(episode_id=17,episode_no=1,episode_name="Episode 3.1",link_list_id=25,desc="this is episode 3.1 description")
episode.save()
episode=Episode(episode_id=17,episode_no=2,episode_name="Episode 3.2",link_list_id=26,desc="this is episode 3.2 description")
episode.save()
episode=Episode(episode_id=17,episode_no=3,episode_name="Episode 3.3",link_list_id=27,desc="this is episode 3.3 description")
episode.save()
episode=Episode(episode_id=17,episode_no=4,episode_name="Episode 3.4",link_list_id=28,desc="this is episode 3.4 description")
episode.save()
episode=Episode(episode_id=17,episode_no=5,episode_name="Episode 3.5",link_list_id=29,desc="this is episode 3.5 description")
episode.save()



















link=Link(link_list_id=15,name="ep1 link1",link="https://youtube.com/",subtitle_list_id=15,quality_id=15)
link.save()
link=Link(link_list_id=16,name="ep1 link2",link="https://youtube.com/",subtitle_list_id=16,quality_id=16)
link.save()

link=Link(link_list_id=17,name="ep1 link3",link="https://youtube.com/",subtitle_list_id=17,quality_id=17)
link.save()

link=Link(link_list_id=18,name="ep1 link4",link="https://youtube.com/",subtitle_list_id=18,quality_id=18)
link.save()
link=Link(link_list_id=19,name="ep1 link5",link="https://youtube.com/",subtitle_list_id=19,quality_id=19)
link.save()

link=Link(link_list_id=20,name="ep2 link1",link="https://youtube.com/",subtitle_list_id=20,quality_id=20)
link.save()

link=Link(link_list_id=21,name="ep2 link2",link="https://youtube.com/",subtitle_list_id=21,quality_id=21)
link.save()

link=Link(link_list_id=22,name="ep2 link3",link="https://youtube.com/",subtitle_list_id=22,quality_id=22)
link.save()

link=Link(link_list_id=23,name="ep2 link4",link="https://youtube.com/",subtitle_list_id=23,quality_id=23)
link.save()

link=Link(link_list_id=24,name="ep2 link5",link="https://youtube.com/",subtitle_list_id=24,quality_id=24)
link.save()
link=Link(link_list_id=25,name="ep3 link1",link="https://youtube.com/",subtitle_list_id=25,quality_id=25)
link.save()

link=Link(link_list_id=26,name="ep3 link2",link="https://youtube.com/",subtitle_list_id=26,quality_id=26)
link.save()

link=Link(link_list_id=27,name="ep3 link3",link="https://youtube.com/",subtitle_list_id=27,quality_id=27)
link.save()

link=Link(link_list_id=28,name="ep3 link4",link="https://youtube.com/",subtitle_list_id=28,quality_id=28)
link.save()

link=Link(link_list_id=29,name="ep3 link5",link="https://youtube.com/",subtitle_list_id=29,quality_id=29)
link.save()
link=Link(link_list_id=29,name="ep3 link5",link="https://youtube.com/",subtitle_list_id=30,quality_id=30)
link.save()

link=Link(link_list_id=29,name="ep3 link5",link="https://youtube.com/",subtitle_list_id=31,quality_id=31)
link.save()
link=Link(link_list_id=29,name="ep3 link5",link="https://youtube.com/",subtitle_list_id=32,quality_id=32)
link.save()



server_name=Server_name(server_name_id=1,server_name="openload")
server_name.save()
server_type=Server_type(server_type_id=1,server_type="download")
server_type.save()
subtitle_list=Subtitle_list(subtitle_list_id=15,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=16,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=17,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=17,subtitle_no=2,subtitle_name_id=5)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=18,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()

subtitle_list=Subtitle_list(subtitle_list_id=19,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=20,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=20,subtitle_no=2,subtitle_name_id=3)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=20,subtitle_no=3,subtitle_name_id=4)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=20,subtitle_no=4,subtitle_name_id=5)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=21,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()

subtitle_list=Subtitle_list(subtitle_list_id=22,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()

subtitle_list=Subtitle_list(subtitle_list_id=23,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=24,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=25,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=26,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=27,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=28,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=29,subtitle_no=1,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=30,subtitle_no=2,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=31,subtitle_no=3,subtitle_name_id=2)
subtitle_list.save()
subtitle_list=Subtitle_list(subtitle_list_id=32,subtitle_no=4,subtitle_name_id=2)
subtitle_list.save()



quality=Quality(quality_id=15,quality_name_id=2)
quality.save()
quality=Quality(quality_id=16,quality_name_id=5)
quality.save()
quality=Quality(quality_id=17,quality_name_id=6)
quality.save()
quality=Quality(quality_id=18,quality_name_id=4)
quality.save()
quality=Quality(quality_id=19,quality_name_id=3)
quality.save()
quality=Quality(quality_id=20,quality_name_id=2)
quality.save()
quality=Quality(quality_id=21,quality_name_id=2)
quality.save()
quality=Quality(quality_id=22,quality_name_id=1)
quality.save()

quality=Quality(quality_id=23,quality_name_id=2)
quality.save()
quality=Quality(quality_id=24,quality_name_id=5)
quality.save()
quality=Quality(quality_id=25,quality_name_id=5)
quality.save()

quality=Quality(quality_id=26,quality_name_id=6)
quality.save()
quality=Quality(quality_id=27,quality_name_id=7)
quality.save()
quality=Quality(quality_id=28,quality_name_id=8)
quality.save()
quality=Quality(quality_id=29,quality_name_id=2)
quality.save()
quality=Quality(quality_id=30,quality_name_id=6)
quality.save()
quality=Quality(quality_id=31,quality_name_id=10)
quality.save()
quality=Quality(quality_id=32,quality_name_id=8)
quality.save()


writer=Writer(writer_id=5,writer_name_id=5)
writer.save()
writer_name=Writer_name(writer_name_id=5,writer_name="games writer")
writer_name.save()

