from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)        # related images are also deleted when a user is deleted
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,                   # for building beautiful SEO-friendly URLs
                            blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)                 # creates an index in the database for this field
    
    def __str__(self):
        return self.title

    # to automatically generate the slug field based on the title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
