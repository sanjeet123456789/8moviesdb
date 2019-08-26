from django import forms
from .models import Subtitle_name

class Subtitle_name_Form(forms.ModelForm):
	class Meta:
		model=Subtitle_name
		fields=[
				'subtitle_name_id',
				'subtitle_name',
				'subtitle_short_code'

		]
\
class Raw_Subtitle_name_Form(forms.Form):
	subtitle_name_id=forms.CharField()
	subtitle_name=forms.CharField()
	subtitle_short_code=forms.CharField()
