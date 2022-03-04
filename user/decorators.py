from django.shortcuts import redirect
from django.http import HttpResponse


def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def is_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if user.groups.all()[0].name == 'admin':
            return redirect('http://127.0.0.1:8000/admin/')
            return HttpResponse('Admins login from Admin Portal')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
