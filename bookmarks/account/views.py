from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':               # 当通过 POST request 调用 user_login 时
        form = LoginForm(request.POST)
        if form.is_valid():                    # 若无效，传入 template 会展示 errors
            cd = form.cleaned_data
            user = authenticate(request,       # authenticate the user against the database
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()                      # 当通过 GET request 调用 user_login 时，创建一个 LoginForm 实例传入 template
    return render(request, 'account/login.html', {'form': form})

# The login_required decorator checks whether the current user is authenticated. 
# If the user is authenticated, it executes the decorated view; 
# if the user is not authenticated, it redirects the user to the login URL 
# with the originally requested URL as a GET parameter named `next` (
# http://127.0.0.1:8000/account/login/?next=/account/).
# http://127.0.0.1:8000/account/
@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
