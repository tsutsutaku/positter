from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Like, Profile, Follow
from rest_framework.response import Response

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
<<<<<<< HEAD
=======
            
>>>>>>> make index UI
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

        #ユーザーがいいねしたかどうか
        like_tf = []
        for i in object_list[::-1]:
            if Like.objects.filter(user=user, post=i).count() == 0:
                like_tf.append(False)
            
            else:
                like_tf.append(True)
        
        zip_l = zip(object_list[::-1], like_tf)
    
        
        
        return render(request, 'home.html', {
            'object_list': zip_l,
            'profile': profile,
            
            
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
    object_list = Post.objects.filter(author=user)
    logined_user = request.user
<<<<<<< HEAD
=======
    
>>>>>>> make index UI

    if Follow.objects.filter(user=logined_user, follow_id=user).count() == 0:
        is_following = False
    
    else:
        is_following = True

    like_tf = []
    for i in object_list[::-1]:
        if Like.objects.filter(user=logined_user, post=i).count() == 0:
            like_tf.append(False)
            
        else:
            like_tf.append(True)
        
    zip_l = zip(object_list[::-1], like_tf)

    followed_n = Follow.objects.filter(user=user).count()
    follower_n = Follow.objects.filter(follow_id=user).count()

    return render(request, 'profile.html', {
        'user': user,
        'object_list': zip_l,
        'logined_user': logined_user,
         'follower_n': follower_n,
        'followed_n': followed_n,
        'is_following': is_following,
    })


def detailfunc(request, pk):
    object=Post.objects.get(pk=pk)
<<<<<<< HEAD
    return render(request, 'detail.html', {'object':object})
=======
    user = request.user

    if Like.objects.filter(user=user, post=pk).count() == 0:
        tf = False
    
    else:
        tf = True


    return render(request, 'detail.html', {'object':object, 'tf':tf})
>>>>>>> make index UI




def likefunc(request, pk):
    if request.method == 'POST':
        post_id = Post.objects.get(pk=pk)
        object_list = Post.objects.all()
        user = request.user
        profile = Profile.objects.get(user=user)

        if Like.objects.filter(user=request.user, post=pk).count() == 0:

            Like.objects.create(user=user, post=post_id)
            post_id.like_num += 1
            post_id.save()

        else:
            Like.objects.filter(user=user, post=post_id).delete()
            post_id.like_num -= 1
            post_id.save()

        data = {
            'object_list': object_list[::-1],
                'profile': profile
        }


        return HttpResponse(data)




def followfunc(request, follow_id):

    username = request.user

    if Follow.objects.filter(user=username, follow_id=follow_id).count() == 0:
        is_following = False
    
    else:
        is_following = True
    
    if is_following:
        Follow.objects.filter(user=username, follow_id=follow_id).delete()
    
    else:
        Follow.objects.create(user=username, follow_id=follow_id)


    
    user = get_object_or_404(User, username=username)
    object_list = Post.objects.filter(author=user)
    

    like_tf = []

    for i in object_list[::-1]:
        if Like.objects.filter(user=username, post=i).count() == 0:
            like_tf.append(False)
            
        else:
            like_tf.append(True)

        
    zip_l = zip(object_list[::-1], like_tf)

    followed_n = Follow.objects.filter(user=user).count()
    follower_n = Follow.objects.filter(follow_id=user).count()

   


    data = {
        'user': user,
        'object_list': zip_l,
        'logined_user': username,
        'follower_n': follower_n,
        'followed_n': followed_n,
        'is_following': is_following,
    }

    return HttpResponse(data)

