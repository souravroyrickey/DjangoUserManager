
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserForm
from .models import NewUser
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated, is_admin
# Create your views here.


def authenticate(username, password):
    UserModel = get_user_model()
    try:
        user = UserModel._default_manager.get(user_name=username)
        if getattr(user, 'is_active', None) and user.check_password(password):
            return user
        else:
            return user
    except UserModel.DoesNotExist:
        return None


@unauthenticated
def registerUser(request):
    form = CustomUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')

            password = form.cleaned_data.get('password1')
            user = NewUser.objects.create_user(
                email=email, user_name=username, role=role, password=password)
            group = Group.objects.get(name=role)
            user.groups.add(group)
            if authenticate(username, password) == None:
                messages.info(request, 'Account not created for'+username)
            messages.info(request, 'Account created for '+username)
            return redirect('login')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated
def loginUser(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        UserModel = get_user_model()
        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("home")
        else:
            messages.error(
                request, f"Invalid username or password.")
    context = {"data": 1}
    return render(request=request, template_name="login.html", context=context)


def logoutUser(request):
    logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(
        request, f"You are logged out sucessfully...")
    return redirect('login')


@login_required(login_url='login')
@is_admin
def homeView(request):
    context = {}
    return render(request, 'home.html', context)
