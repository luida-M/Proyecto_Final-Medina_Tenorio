from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'accounts/base.html')  # Vista para la base

def servicios(request):
    return render(request, 'accounts/servicios.html')  # Vista para 'servicios'

def vacantes(request):  # Corregido el nombre de 'porfolio_view' a 'portfolio_view'
    return render(request, 'accounts/vacantes.html')  # Vista para 'vacantes'

def nosotros(request):
    return render(request, 'accounts/nosotros.html')  # Vista para 'nosotros'

def clientes(request):
    return render(request, 'accounts/clientes.html')  # Vista para 'clientes'

def contacto(request):
    return render(request, 'accounts/contacto.html')  # Vista para 'contacto'
