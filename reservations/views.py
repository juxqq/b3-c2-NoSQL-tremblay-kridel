from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Ecole
from .forms import EcoleSignupForm
from django.contrib.auth.models import Group

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
            group = Group.objects.get(name='User')
            user.groups.add(group)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'title': 'Créer un compte'})

def signout(request):
    logout(request)
    return redirect('/reservations/login')

def account_type(request):
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        if account_type == 'ecole':
            return redirect('ecole_signup')
        elif account_type == 'user':
            return redirect('signup')
    return render(request, 'account_type.html')

def ecole_signup(request):
    if request.method == 'POST':
        form = EcoleSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form_nom = form.cleaned_data.get('nom')
            form_adresse = form.cleaned_data.get('adresse')
            form_ville = form.cleaned_data.get('ville')
            form_codePostal = form.cleaned_data.get('codePostal')
            Ecole.objects.create(
                nom=form_nom, 
                adresse=form_adresse, 
                ville=form_ville, 
                codePostal=form_codePostal)
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            group = Group.objects.get(name='Ecole')
            user.groups.add(group)
            return redirect('login')
    else:
        form = EcoleSignupForm()
    return render(request, 'ecole_signup.html', {'form': form, 'title': 'Créer un compte pour l\'école'})