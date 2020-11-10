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

Use the management command runserver_plus provided by Django Extensions to run the development server:
`python manage.py runserver_plus --cert-file cert.crt`

测试 HTTP**S**：https://mysite.com:8000/account/login/

You can now serve your site through HTTPS during development in order to test social authentication with Facebook, Twitter, and Google.

#### Authentication using Facebook
略
#### Authentication using Twitter

#### Authentication using Google
略

# Sharing Content
1. Define a model to store images and their information
2. Create a form and a view to handle image uploads
3. Build a system for users to be able to post images that they find on external websites

## Creating an image bookmarking website

`django-admin startapp images`

### Creating many-to-many relationships
1. define the `Image` model
2. create an initial migration: `python manage.py makemigrations images`
3. apply the migration (synce `Image` model to the database): `python manage.py migrate images`
### Registering the image model in the administration site
`python manage.py runserver_plus --cert-file cert.crt`

https://127.0.0.1:8000/admin/

## Posting content from other websites
In order to use the urllib to retrieve images from URLs served through HTTPS, you need to install the `Certifi Python` package. 

`pip install --upgrade certifi`

https://127.0.0.1:8000/images/create/?**title=...**&**url=...**

https://127.0.0.1:8000/images/create/?title=%20Django%20and%20Duke&url=https://upload.wikimedia.org/wikipedia/commons/8/85/Django_Reinhardt_and_Duke_Ellington_%28Gottlieb%29.jpg.

提交后，get_absolute_url 未定义，但图片已保存：https://127.0.0.1:8000/admin/images/image/

### Building a bookmarklet with jQuery
