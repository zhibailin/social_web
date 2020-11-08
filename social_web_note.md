`python manage.py migrate`

http://127.0.0.1:8000/admin
http://127.0.0.1:8000/account/login/

处理用户照片需要图像处理库：
`pip install Pillow==7.0.0`

Django 对静态文件的服务很低效，只能用于开发环境，不能用产品环境。

`python manage.py makemigrations`
`python manage.py migrate`

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/admin/account/edit
显示诸如“修改成功”的反馈信息

 add an authentication backend to let users authenticate in your site using their email address instead of their username.

 http://127.0.0.1:8000/account/login/ 

### social authentication
Python Social Auth is a Python module that simplifies the process of adding social authentication to your website.
`pip install social-auth-app-django==3.1.0`

sync Python Social Auth models with your database
`python manage.py migrate`

在 `/etc/hosts` 中添加一行：
`127.0.0.1 mysite.com`

测试：http://mysite.com:8000/account/login

### Running the development server through HTTPS

**Django Development server** 无法通过 HTTPS 为您的网站提供服务，因为这不是其预期用途。需要 `RunServerPlus` extension。
注意：Django Extensions 仅可用于开发环境，不能用于产品环境。

`pip install django-extensions==2.2.5`

`pip install werkzeug==0.16.0`

`pip install pyOpenSSL==19.0.0`
