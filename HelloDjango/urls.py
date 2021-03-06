from django.conf.urls import url
from django.urls import path
from . import hello, testdb
from django.contrib import admin

urlpatterns = [
    # url(r'^$', view.hello),
    path('', hello.index),
    path('hello/', hello.hello),
    url(r'^userSave$', testdb.save),
    url('userDelete', testdb.delete),
    url('userUpdate', testdb.update),
    url('usersList', testdb.select),
    url('userCreate', testdb.userCreate),
    url(r'^admin/', admin.site.urls), # django web管理工具
]
