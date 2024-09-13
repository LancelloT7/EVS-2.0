from django.shortcuts import render, redirect

# Create your views here.
def options(request):
    return render(request, 'menu_principal/options.html')