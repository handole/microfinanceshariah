from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm

# Create your views here.
def register(request):
	return render(request, '/', {})

def login(request):
	return render(request, '', {})

def logout(request):
	pass