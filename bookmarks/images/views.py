from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

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
            # TODO: implemented the get_absolute_url() method of the Image model
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET by the JavaScript tool
        # TODO: the JavaScript tool
        form = ImageCreateForm(data=request.GET)
    
    return render(request,
                  'images/image/create.html',
                  {
                      'section': 'images',
                      'form': form,
                  })
