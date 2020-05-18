from django.conf.urls import url
from django.urls import path
from . import hello, testdb

urlpatterns = [
    # url(r'^$', view.hello),
    path('', hello.index),
    path('hello/', hello.hello),
    url(r'^savedb$', testdb.save),
    url(r'^deletedb$', testdb.delete),
    url(r'^updatedb$', testdb.update),
    url(r'^selectdb$', testdb.select),
]
