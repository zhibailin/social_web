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

    # to verify that the provided image URL is valid, only allow JPEG files
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url
