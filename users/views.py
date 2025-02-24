from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserSearchForm
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            Profile.objects.create(user=user)  # Создаем профиль
            login(request, user)
            return redirect("profile")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("profile")
    return render(request, "users/login.html")

@login_required
def profile(request):
    profile = request.user.profile
    return render(request, "users/profile.html", {"profile": profile})

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "users/edit_profile.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")

def user_search(request):
    users = []
    form = UserSearchForm()
    
    if request.method == "GET" and "query" in request.GET:
        form = UserSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            users = User.objects.filter(username__icontains=query)
    
    return render(request, "users/user_search.html", {"form": form, "users": users})
    