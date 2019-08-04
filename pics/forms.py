from django import forms 
from .models import *
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = pics 
        fields = ['image_id', 'pic_link']