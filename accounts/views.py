from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from results.models import StudentProfile

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        roll_no = request.POST['roll_no']
        year = request.POST['year']
        semester = request.POST['semester']

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('/register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('/register')

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        StudentProfile.objects.create(
            user=user,
            roll_no=roll_no,
            year=year,
            semester=semester
        )
        messages.success(request, 'Account created! Please login.')
        return redirect('/login')
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('/login')
