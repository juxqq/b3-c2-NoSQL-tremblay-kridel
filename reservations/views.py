from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'Login'})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'title': 'Create Account'})

def signout(request):
    logout(request)
    return redirect('/reservations/login')

def account_type(request):
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        if account_type == 'ecole':
            return redirect('school_signup')
        elif account_type == 'user':
            return redirect('signup')
    return render(request, 'account_type.html')

def school_signup(request):
    if request.method == 'POST':
        # Process form data here
        return redirect('home')
    return render(request, 'school_signup.html')