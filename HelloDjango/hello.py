from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    index = "<p>index page</p>"
    index += "<div><ul>"
    index += "<li><a href='/hello'>hello</a></li>"
    index += "<li><a href='/users'>users</a></li>"
    index += "</ul></div>"
    return HttpResponse(index)

def hello(request):
    context          = {}
    context['hello'] = 'Hello Django!'
    context['num'] = 108
    context['list'] = ['Tanglong','Lexie','Test']
    return render(request, 'hello.html', context)