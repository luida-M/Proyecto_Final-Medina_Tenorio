from django.shortcuts import render
from .models import Desarrollador

# Create your views here.

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

def desarrollador(request):
    return render(request, 'accounts/desarrollador.html')


def desarrollador(request):
    if request.method == 'POST':
        desarrollador = Desarrollador(name=request.POST['desarrollador'], rol=request.POST['rol'], email=request.POST['email'])
        desarrollador.save()
        return render(request, 'accounts/base.html')
    return render(request, 'accounts/desarrollador.html')
