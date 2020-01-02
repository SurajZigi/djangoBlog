from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Suraj',
        'title': 'Blog Post 1',
        'content': 'First post Content',
        'date_posted': 'January 1, 2020'
    },
    {
        'author': 'Aman',
        'title': 'Blog Post 2',
        'content': 'Second post Content',
        'date_posted': 'January 2, 2020'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
     return render(request, 'blog/about.html')