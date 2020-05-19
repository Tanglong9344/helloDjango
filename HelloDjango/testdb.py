# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from helloModel.models import users

# 数据库操作
# insert
def save(request):
    id = request.POST.get("id")
    if id is not None:
        return update(request)
    name = request.POST.get("name")
    print('name:',name)
    if name is None:
        return HttpResponse("<p>姓名不允许为空！</p>")
    age = request.POST.get("age")
    if age is None:
        age = 0
    description = request.POST.get("description",'')
    user = users(name=name,age=age,description=description)
    user.save()
    return HttpResponse("<p>数据添加成功！</p><a href='/users'>返回</a></p></p>")

# delete
def delete(request):
    id = request.GET.get("id")
    if id is None:
        return HttpResponse("<p>Id不允许为空！</p>")
    user = users.objects.get(id=id)
    user.delete()
    return HttpResponse("<p>数据删除成功！<p><a href='/users'>返回</a></p></p>")

# update
def update(request):
    id = request.POST.get("id")
    if id is None:
        return HttpResponse("<p>Id不允许为空！</p>")
    user = users.objects.get(id=id)
    name = request.POST.get("name")
    if name is not None:
        user.name = name
    age = request.POST.get("age")
    if age is not None:
        user.age = age
    description = request.POST.get("description")
    if description is not None:
        user.description = description
    user.save()
    return HttpResponse("<p>数据更新成功！</p><p><a href='/users'>返回</a></p>")

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
    return render(request, 'usersList.html', context)

# create or update user
def userCreate(request):
    type = int(request.GET.get("type"))
    if type is None:
        type = 0
    context = {}
    if type == 1 or type == 2:
        id = request.GET.get("id")
        user = users.objects.get(id=id)
        context['user'] = user
        context['type'] = type
    return render(request, 'userCreate.html',context)