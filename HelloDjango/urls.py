from django.conf.urls import url
from django.urls import path
from . import hello, testdb

urlpatterns = [
    # url(r'^$', view.hello),
    path('', hello.index),
    path('hello/', hello.hello),
    url(r'^userSave$', testdb.save),
    url('userDelete', testdb.delete),
    url('userUpdate', testdb.update),
    url('users', testdb.select),
    url('userCreate', testdb.userCreate),
]
