from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistratinForm

 
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistratinForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for { username }!')
            return redirect('blog-home')
    else: 
        form = UserRegistratinForm()
    return render(request,'users/register.html', {'form': form})
 