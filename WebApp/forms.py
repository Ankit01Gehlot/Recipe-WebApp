from django import forms 
from .models import Dish

class DishForm(forms.ModelForm):
    
    class Meta:
        model = Dish 
        fields = ('title','tag','ingredients','imageUrl','direction','timeToCook')