from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


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
    
    # to download the image file and save it
    def save(self, force_insert=False,
                   force_update=False,
                   commit=True):
        image = super().save(commit=False)              # create a new image instance
        image_url = self.cleaned_data['url']
        name = slugify(image.title)                     # generate the image name
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        
        # download image from the given URL and save it
        response = request.urlopen(image_url)
        image.image.save(image_name,
                         ContentFile(response.read()),  # save the file to the media directory
                         save=False)                    # avoid saving the object to the database
        if commit:                                      # to maintain the same behavior as the save() method you override
            image.save()                                # you save the form to the database only when the commit parameter is True
        return image
