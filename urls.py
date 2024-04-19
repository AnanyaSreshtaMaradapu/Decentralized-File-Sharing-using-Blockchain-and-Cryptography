
"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('u_', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('u_', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('u_blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [


    path('', views.homepage, name="n_home"),
    path('home/', views.home, name="home"),
    path('a_loginaction/', views.adminloginaction, name="a_loginaction"),
    path('a_adminhome/', views.adminhomedef, name="adminhomedef"),
    path('a_adminlogout/', views.adminlogoutdef, name="adminlogoutdef"),
    
    
    path('u_loginaction/', views.userloginaction, name="n_loginaction"),
    path('u_signup/', views.signuppage, name="n_signup"),
    
    path('u_userhome/', views.userhomedef, name="userhomedef"),
    path('u_userlogout/', views.userlogoutdef, name="userlogoutdef"),
    path('u_viewprofile/', views.viewprofilepage, name="n_viewprofile"),
    path('fileupload/', views.fileupload, name="fileupload"),
    path('fileupload2/', views.fileupload2, name="fileupload2"),
    path('viewfiles/', views.viewfiles, name="viewfiles"),
    path('viewfile/<str:op>/', views.viewfile, name="viewfile"),
    path('lviewfile/<str:op>/', views.lviewfile, name="lviewfile"),
    path('delete/<str:op>/', views.delete, name="delete"),
    
    path('inbox/', views.inbox, name="inbox"),
    path('inbox2/<str:op>/', views.inbox2, name="inbox2"),
    path('inboxdecrypt/', views.inboxdecrypt, name="inboxdecrypt"),
    
    path('updateprofile/', views.updateprofile, name="updateprofile"),
    path('updatepwd/', views.updatepwd, name="updatepwd"),    
    path('filesave/', views.filesave, name="filesave"),

    
]
