# Hello Django
+ Django 命令
    + 创建项目helloDjango:django-admin startproject helloDjango
    + 创建模型helloModel:django-admin startapp helloModel
    + 创建表结构
        + python manage.py migrate # 创建默认表
        + python manage.py makemigrations helloModel # 通知django model 发生了变化
        + python manage.py migrate helloModel # 创建表结构
    + 启用Django web管理工具，创建超级用户： python manage.py createsuperuser
    + 启动项目：manage.py runserver port
+ 所需python库

|名称|命令|
|:---:|:---:|
|Django|pip install django|
|Mysql|pip install mysqlclient|