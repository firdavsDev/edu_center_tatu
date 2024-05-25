from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is taken')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                # here login the user
                login(request, user)
                messages.success(request, 'Account created successfully')
                return redirect('home')
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')
