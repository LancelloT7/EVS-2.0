from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def cadastrar(request):
    return render(request, 'cadastrar.html')
def triagem(request):
    return render(request, 'triagem.html')

