from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Like

# Create your views here.


def signupfunc(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            login(request, authenticate(request, username=username2, password=password2))
            return redirect('login')
    return render(request, 'signup.html')



def loginfunc(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error':'無効なログインです。ユーザーネームかパスワードを確認してください。'})

    return render(request, 'login.html')


def indexfunc(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        return render(request, 'index.html')


def homefunc(request):
    object_list = Post.objects.all()
    if  request.user.is_authenticated:
        return render(request, 'home.html', {'object_list':object_list})

    else:
        return redirect('index')
        



def logoutfunc(request):
    logout(request)
    return redirect('home')
