from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def base(request):
    return render(request, 'accounts/base.html')

def team(request):
    return render(request, 'accounts/team.html')

def portfolio(request): 
    return render(request, 'accounts/portfolio.html')

def services(request):
    return render(request, 'accounts/services.html')  # Asegúrate de que el nombre y la ruta coincidan

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')
