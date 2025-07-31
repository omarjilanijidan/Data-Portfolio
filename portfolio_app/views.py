# portfolio_app/views.py
from django.shortcuts import render
from .models import Technology, Service, Project

def home(request):
    context = {
        'technologies': Technology.objects.all(),
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'page': 'home'
    }
    return render(request, 'portfolio_app/home.html', context)

def about(request):
    context = {'page': 'about'}
    return render(request, 'portfolio_app/about.html', context)

def contact(request):
    if request.method == 'POST':
        return render(request, 'portfolio_app/contact_success.html')
    context = {'page': 'contact'}
    return render(request, 'portfolio_app/contact.html', context)