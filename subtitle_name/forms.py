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

class Raw_Subtitle_name_Form(forms.Form):
	subtitle_name_id=forms.IntegerField()
	subtitle_name=forms.CharField()
	subtitle_short_code=forms.CharField()


class update_Subtitle_name_Form(forms.ModelForm):
	class Meta:
		model=Subtitle_name
		fields=['subtitle_name_id','subtitle_name','subtitle_short_code']

		# def update_subtitle(self,*args,**kwargs):
		# 	instance=self.instance
		# 	subtitle_name_id=self.cleaned_data.get('subtitle_name_id')
		# 	print(subtitle_name_id)
		# 	qs=Subtitle_name.object.filter(subtitle_name_iexact=subtitle_name_id)
		# 	if instance is not None:
		# 		qs=qs.exclude(pk=instance.pk)

		# 	if qs.exist():
		# 		raise forms.ValidationError("This title has already been used Please insert new value")
		# 	return subtitle_name_id