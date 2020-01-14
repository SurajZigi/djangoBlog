from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView #creating a list view so import
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
    

#creating a list view 
class PostListView(ListView):
    model  = Post
    template_name = 'blog/home.html'
    context_object_name ='posts' 
    ordering = ['-date_psoted']
    #<app>/<model>_<viewtype>.html 

class PostDetailView(DetailView):
    model  = Post

class PostCreateView(CreateView):
    model  = Post
    fields = ['title', 'content']


def about(request):
     return render(request, 'blog/about.html',{'title':'About'})