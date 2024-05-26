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
            messages.success(request, 'Muaffaqiyatli kirdingiz!')
            return redirect('home')
        else:
            messages.error(request, 'Login yoki parol xato!')
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu foydalanuvchi nomi band')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Bu email band')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                # here login the user
                login(request, user)
                messages.success(
                    request, 'Muvaffaqiyatli ro`yxatdan o`tdingiz!')
                return redirect('home')
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')
