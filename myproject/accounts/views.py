from django.shortcuts import render
from .models import Desarrollador, Cliente

def base(request):
    return render(request, 'accounts/base.html')

def team(request):
    return render(request, 'accounts/team.html')

def portfolio(request): 
    return render(request, 'accounts/portfolio.html')

def services(request):
    return render(request, 'accounts/services.html')
def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def desarrollador(request):
    return render(request, 'accounts/desarrollador.html')

def cliente(request):
    return render(request, 'accounts/form_cliente.html')

def desarrollador(request):
    if request.method == 'POST':
        desarrollador = desarrollador(name=request.POST['desarrollador'], rol=request.POST['rol'], email=request.POST['email'])
        desarrollador.save()
        return render(request, 'accounts/base.html')
    return render(request, 'accounts/desarrollador.html')

def form_cliente(request):
    if request.method == 'POST':
        cliente = cliente(name=request.POST['name'], company=request.POST['company'], email=request.POST['email'], elefono=request.POST['telefono'],
            mensaje=request.POST['mensaje'])
        cliente.save()
        return render(request, 'accounts/base.html', {"message": "Cliente registrado correctamente"})
    return render(request, 'accounts/form_cliente.html')