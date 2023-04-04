import uuid
from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Ecole(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=250)
    ville = models.CharField(max_length=50)
    codePostal = models.CharField(max_length=5)

class Reservation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
