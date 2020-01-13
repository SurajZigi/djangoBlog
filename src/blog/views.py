from django.shortcuts import render
from django.views.generic import ListView #creating a list view so import
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
    
    #<app>/<model>_<viewtype>.html 



def about(request):
     return render(request, 'blog/about.html')