from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    index = "<p>index page</p>"
    index += "<div><ul>"
    index += "<li><a href='/hello'>hello</a></li>"
    index += "<li><a href='/usersList'>users</a></li>"
    index += "</ul></div>"
    return HttpResponse(index)

def hello(request):
    path = request.path
    print("path:{}".format(path))

    method = request.method
    print("method:{}".format(method))

    body = request.body
    print("body:",body)

    context          = {}
    context['hello'] = 'Hello Django!'
    context['num'] = 108
    context['list'] = ['Tanglong','Lexie','Test']
    return render(request, 'hello.html', context)