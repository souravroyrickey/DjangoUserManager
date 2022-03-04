from django.urls import URLPattern, path, include
from . import views
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from django.shortcuts import redirect

admin.site.site_header = "Student Admin"
admin.site.site_title = "Student Admin Portal"
admin.site.index_title = "Welcome to Student Portal"

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('home/', views.homeView, name='home'),
    path('', views.logoutUser, name='logout'),
    path('', lambda _: redirect('admin:index'), name="index")
]
