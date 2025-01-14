# forms.py
from django import forms
from .models import CandidateRestaurant

class CandidateRestaurantForm(forms.ModelForm):
    class Meta:
        model = CandidateRestaurant
        fields = ['display_name', 'photos', 'review']
