from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('', views.indexfunc, name='index'),
    path('logout/', views.logoutfunc, name='logout'),
    path('home/', views.homefunc, name='home'),
    path('create/', views.createfunc, name='create'),
    path('profile/<str:username>/', views.profilefunc, name='profile'),
]