from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
 

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
            return redirect('login')

    return render(request, 'login.html')

@login_required
def homefunc(request):
    return render(request, 'home.html')

def logoutfunc(request):
    logout(request)
    return redirect('login')