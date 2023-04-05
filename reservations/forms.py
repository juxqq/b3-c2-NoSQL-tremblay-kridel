from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class EcoleSignupForm(UserCreationForm):
    nom = forms.CharField(max_length=30, required=True)
    adresse = forms.CharField(max_length=100, required=True)
    ville = forms.CharField(max_length=50, required=True)
    codePostal = forms.CharField(max_length=10, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'nom', 'adresse', 'ville', 'codePostal', 'password1', 'password2']