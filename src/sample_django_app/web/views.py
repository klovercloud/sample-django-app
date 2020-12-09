from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    resp = render(request, 'web/templates/index.html')
    return resp

def health(request):
    return HttpResponse("I am live :)")
