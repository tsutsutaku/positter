from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('home/', views.homefunc, name='home'),
    path('logout/', views.logoutfunc, name='logout'),
]