from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # change password urls
    path('password_change/',   #  http://127.0.0.1:8000/account/password_change/
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # reset password urls
    # 邮箱表单页
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    # 邮件发送完成页
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    # 密码重置表单页
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    # 完成密码重置
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
