from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserRegisterForm
from django.contrib import messages

 
# Create your views here. 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f'Your account has been created now you can login')
            return redirect('login')
    else: 
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form': form})
 