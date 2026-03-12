from django import forms
from . import models

class CreatePhoto(forms.ModelForm):
    class Meta: 
        model = models.Photo
        fields=['title', 'picture']
