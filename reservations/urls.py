from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name="signout"),
    path('account_type', views.account_type, name="account_type"),
    path('ecole_signup', views.ecole_signup, name="ecole_signup"),
]