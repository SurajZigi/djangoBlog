from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
# Create your views here.
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostCreateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
 ]
#<app>/<model>_<viewtype>.html 