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

模板中，`<!-- -->` 注释中不能有 template tag，比如 `<!-- {% with %} -->`

测试：
1. https://127.0.0.1:8000/account/ 将 `Bookmark it` 按钮拖到书签栏
2. 打开亚马逊或者京东，点击 `Bookmark it`
3. 访问的图片网站必须是 HTTPS。浏览器会阻止您在通过 HTTPS 服务的网站上运行基于 HTTP的 bookmarklet。
>For security reasons, your browser will prevent you from running the bookmarklet over HTTP on a site served through HTTPS. You will need to be able to load the bookmarklet on any site, including sites secured through HTTPS. To run your development server using an auto-generated SSL/TLS certificate, you will use RunServerPlus from Django Extensions, which you installed in the previous chapter.

`python manage.py runserver_plus --cert-file cert.crt`

### Creating image thumbnails using easy-thumbnails
`pip install easy-thumbnails==2.7`

`python manage.py migrate`

### Adding AJAX actions with jQuery
加载 jQuery 的 2 种方式：
1. load the jQuery framework from Google's CDN. 
2. download jQuery from https://jquery.com/ and add it to the static directory.

测试：https://127.0.0.1:8000/images/
若要删除图片，需要登录后台操作

# Tracking User Action
## follow system

`python manage.py makemigrations account`
`python manage.py migrate account`

user list 测试：
`python manage.py runserver`
http://127.0.0.1:8000/account/users/

## activity stream
`python manage.py startapp actions`
 
 create initial migrations for "action" application
 `python manage.py makemigrations actions`

sync the application with the database
`python manage.py migrate`

测试 http://127.0.0.1:8000/account/

## denormalization and signals
场景：获取最受欢迎的 images。
实现：利用聚合函数统计出 `total_likes` 并排序
```python 
from django.db.models import Count
from images.models import Image

images_by_popularity = Image.objects.annotate(total_likes=Count('users_like'))\
                                    .order_by('-total_likes')
```
但是，该方法性能开销很大，优化方案是：
- denormolize `total_likes` -- 将 `total_likes` 作为一个新的字段添加到 `Image` model。
- 问题是如何保持该字段的更新 -- 使用 *Django signals*

### 1. denormalization：在 model 中添加字段并 migrate
`python manage.py makemigrations images`
`python manage.py migrate images`

### 2. 创建 receiver function
### 3. 将 receiver function 连接到 signal
import `signals` module in the `ready()` mehtod of the **application configuration class**.
