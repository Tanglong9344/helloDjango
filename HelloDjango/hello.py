from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("index page")

def hello(request):
    context          = {}
    context['hello'] = 'Hello Django!'
    context['num'] = 108
    context['list'] = ['Tanglong','Lexie','Test']
    return render(request, 'hello.html', context)