from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image


@login_required # 登录了才能操作
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # if form data is valid, create a new Image instance, not be saved to the database
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            
            # who uploaded each image: assign current user to the new `image` object
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            
            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET by the JavaScript tool
        form = ImageCreateForm(data=request.GET)
    
    return render(request,
                  'images/image/create.html',
                  {
                      'section': 'images',
                      'form': form,
                  })

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                  'images/image/detail.html',
                  {
                      'section': 'images',
                      'image': image,
                  })
