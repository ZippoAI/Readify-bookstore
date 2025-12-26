from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
        

    return render(request, 'userAuth/login.html')










def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not all ([username, email, password]):
            messages.error(request, 'All fields are required')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
    

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        login(request, user)
        return redirect('home')


    return render(request, 'userAuth/register.html')


def user_logout(request):
    logout(request)
    return redirect('home')