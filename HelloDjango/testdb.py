# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from helloModel.models import users

# 数据库操作
# insert
def save(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("<p>姓名不允许为空！</p>")
    age = request.GET.get("age")
    if age is None:
        age = 0
    description = request.GET.get("description",'')
    user = users(name=name,age=age,description=description)
    user.save()
    return HttpResponse("<p>数据添加成功！</p>")

# delete
def delete(request):
    id = request.GET.get("id")
    if id is None:
        return HttpResponse("<p>Id不允许为空！</p>")
    user = users.objects.get(id=id)
    user.delete()
    return HttpResponse("<p>数据删除成功！</p>")

# update
def update(request):
    id = request.GET.get("id")
    if id is None:
        return HttpResponse("<p>Id不允许为空！</p>")
    user = users.objects.get(id=id)
    name = request.GET.get("name")
    if name is not None:
        user.name = name
    age = request.GET.get("age")
    if age is not None:
        user.age = age
    description = request.GET.get("description")
    if description is not None:
        user.description = description
    user.save()
    return HttpResponse("<p>数据更新成功！</p>")

# select
def select(request):
    list = users.objects
    id = request.GET.get("id")
    if id is not None:
        list = list.filter(id=id)
    name = request.GET.get("name")
    if name is not None:
        list = list.filter(name__contains=name) # 模糊查询
    list = list.all().order_by('-name') # 按姓名降序
    context = {}
    context['list'] = list
    return render(request, 'users.html', context)