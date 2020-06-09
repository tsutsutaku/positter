from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Like, Profile

import re
# Create your views here.


def checkAlnum(word):
    alnum = re.compile(r'^[a-zA-Z0-9]+$')
    result = alnum.match(word) is not None
    return result


def signupfunc(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        displayname = request.POST['displayname']

        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            if not checkAlnum(username2):
                return render(
                    request, 'signup.html',
                    {'validate_error': '無効なidです。idには半角英数字のみ使用してください'})

            user = User.objects.create_user(username2, '', password2)
            login(
                request,
                authenticate(request, username=username2, password=password2))

            Profile.objects.create(display_name=displayname, user=user)
            user.save()
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
            return render(request, 'login.html',
                          {'error': '無効なログインです。ユーザーネームかパスワードを確認してください。'})

    return render(request, 'login.html')


def indexfunc(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        return render(request, 'index.html')


def homefunc(request):
    object_list = Post.objects.all()
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        return render(request, 'home.html', {
            'object_list': object_list,
            'profile': profile
        })

    else:
        return redirect('index')


def logoutfunc(request):
    logout(request)
    return redirect('home')


def createfunc(request):
    if request.method == 'POST':
        text2 = request.POST['text']

        user = request.user
        Post.objects.create(text=text2, author=user)

        return redirect('home')

    if request.user.is_authenticated:
        return render(request, 'create.html')

    else:
        return redirect('signup')


def profilefunc(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})