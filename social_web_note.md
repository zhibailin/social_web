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
