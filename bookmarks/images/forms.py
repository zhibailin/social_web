from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        
        # override the default widget of the `url` field to use a HiddenInput widget.
        # this field is not visible to users
        widgets = {
            'url': forms.HiddenInput,           
        }
