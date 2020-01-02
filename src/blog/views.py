from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>hello this is first template inline</h1>')

def about(request):
    return HttpResponse('<h1>About page</h1>')