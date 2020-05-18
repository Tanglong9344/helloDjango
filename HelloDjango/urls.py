from django.urls import path
from . import view

urlpatterns = [
    # url(r'^$', view.hello),
    path('', view.index),
    path('hello/', view.hello),
]
