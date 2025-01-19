from django.shortcuts import render #get_object_or_404
from accounts.forms import BuscaDesarrolladorForm, FormCliente
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Proyecto, Cliente, Desarrollador
from django.urls import reverse_lazy
from users.models import Imagen
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

def home(request):
    imagen_query = Imagen.objects.filter(user=request.user.id)
    if imagen_query.exists() and len(imagen_query) > 1:
        imagen = imagen_query[1]
    else:
    # Manejar el caso en que no haya suficientes elementos
        imagen = None  # O algún valor por defecto
        print(imagen)
    return render(request, 'accounts/home.html')

def index(request): 
    return render(request, 'accounts/index.html')

def login_request(request):
    msg_login=""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, accounts/home.html)
        msg_login = "Usuario o contraseña incorrecto"            
    form = AuthenticationForm
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})
        

@login_required
def about(request):
    return render(request, 'users/about.html') 

# vista basada en clases - Desarrollador
class DesarrolladorListView(ListView):
    model = Desarrollador
    template_name="accounts/proyecto_list.html"

    def get_queryset(self):
        return Curso.objects.filter(id__lte=10)

class DesarrolladorDetailView(DetailView):
    model = Desarrollador
    template_name = "accounts/desarrollador_detail.html"
    login_url = '/users/login/'

    def get_login_url(self):
        return self.login_url

class DesarrolladorCreateView(CreateView):
    model = Desarrollador
    template_name = "accounts/desarrollador_create.html"
    fields = ["nombre", "rol"]
    success_url = reverse_lazy("DesarrolladorList")    

class DesarrolladorUpdateView(UpdateView):
    model = Desarrollador
    success_url = reverse_lazy("DesarrolladorList")
    fields = ["nombre", "rol"]
    template_name = "accounts/desarrollador_update.html"


class DesarrolladorDeleteView(DeleteView):
    model = Desarrollador
    success_url = reverse_lazy("DesarrolladorList")
    template_name = 'accounts/desarrollador_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        print(f"\n\nESTE METODO SE EJECUTA\n\n")
        if request.user.is_superuser:
            super().post(request, *args, **kwargs)
        return render(request, "accounts/home.html")

# VISTAS BASADAS EN CLASES - Clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = "accounts/proyecto_list.html"
    context_object_name = 'clientes'

    def get_queryset(self, request, *args, **kwargs):
        return super().get(request,*args, **kwargs)

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "accounts/cliente_detail.html"
    model = Proyecto
    login_url = '/users/login/'

    def get_login_url(self):
        return self.login_url


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "accounts/cliente_create.html"
    fields = ["nombre", "empresa", "email"]
    success_url = reverse_lazy("ClienteList")

class ClienteUpdateView(UpdateView):
    model = Cliente
    success_url = reverse_lazy("ClienteList")
    fields = ["nombre", "apellido", "email"]
    template_name = "accounts/cliente_update.html"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("ClienteList")
    template_name = 'accounts/cliente_confirm_delete.html'    

    def post(self, request, *args, **kwargs):
        print(f"\n\n Este Método se ejecuta\n\n")
        if request.user.is_superuser:
            super().post(request, *args, **kwargs)
        return render(request, accounts/home.html)     

# vista basada en clases: Proyecto
class ProyectoListView(ListView):
    model = Proyecto
    template_name='accounts/proyecto_list.html'
   
    def get_queryset(self):
        return Proyecto.objects.filter(id__lte=10)
            
class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'accounts/proyecto_detail.html'
    login_url = '/users/login/'

    def get_login_url(self):
        return self.login_url

class ProyectoCreateView(CreateView):
    model = Proyecto
    template_name = "accounts/proyecto_create.html"
    fields = ["nombre_proyecto", "descripcion", "cliente", "estado", "fecha_inicio", "fecha_fin"]
    success_url = reverse_lazy("ProyectoList")    

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    fields = ["nombre_proyecto", "descripcion", "cliente", "estado", "fecha_inicio", "fecha_fin"]
    template_name = "accounts/proyecto_update.html"
    success_url = reverse_lazy("ProyectoList")

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = "accounts/proyecto_confirm_delete.html"
    success_url = reverse_lazy("ProyectoList")

    def post(self, request, *args, **kwargs):   
        print(f"\n\n Este Método se ejecuta\n\n")
        if request.user.is_superuser:
            super().post(request, *args, **kwargs)
        return render(request, accounts/home.html)         


def form_desarrollador(request):
    if request.method == 'POST':
        informacion = request.POST
        desarrollador = Desarrollador( name=informacion['nombre'], rol=informacion['rol'], email=informacion['email'])
        desarrollador.save()
        return render(request, 'accounts/home.html')  #{'message': 'Desarrollador guardado exitosamente'})
    return render(request, 'accounts/form_desarrollador.html')

def form_cliente(request):
    if request.method == 'POST':
        cliente = Cliente(name=request.POST['nombre'], company=request.POST['company'], email=request.POST['email'], telefono=request.POST['telefono'])
        cliente.save()
        return  render(request, 'accounts/home.html', {"message": "Cliente registrado correctamente"})
    return render(request, 'accounts/form_cliente.html')

def buscar_desarrollador(request):
    if request.method == 'POST':
        form = BuscaDesarrolladorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            desarrolladores = Desarrollador.objects.filter(nombre__icontains=nombre)
            return render(request, 'resultados_desarrolladores.html', {'desarrolladores': desarrolladores, 'form': form})
    else:
        form = BuscaDesarrolladorForm()
    return render(request, 'buscar.html', {'form': form})

def form_con_api (request):
   if request.method == 'POST':
    mi_formulario = InfDesarrollador(request.POST)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        desarrollador = Desarrollador(name=informacion['desarrollador'], proyecto=informacion['proyecto'], email=informacion['email'])
        desarrollador.save()
        return  render(request,'accounts/home.html')
    else:  
        mi_formulario = InfDesarrollador()
        print (f"\n\n{mi_formulario}\n\n")


    return render(request, 'accounts/form_con_api.html', {"mi_formulario": mi_formulario}) 

def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaDesarrollador(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            desarrolladores = Desarrollador.objects.filter(name__icontains=informacion['desarrollador'])
            return render(request, 'accounts/resultados.html', {"desarrolladores": desarrolladores})
    else:
            mi_formulario = BuscaDesarrollador()
            return render(request,'accounts/buscar_form_con_api.html', {"mi_formulario": mi_formulario})
# en esta seccio
def about(request):
    return render(request, 'accounts/about.html')

def team(request):
    return render(request, 'accounts/team.html')

def portfolio(request): 
    return render(request, 'accounts/portfolio.html')

def services(request):
    return render(request, 'accounts/services.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def form_Desarrollador(request):
    return render(request, 'accounts/desarrollador.html')


#def form_Cliente(request):
#    return render(request, 'accounts/form_cliente.html')



 #@login_required
 #def editar_perfil(request):
  #  usuario = request.user
   # if request.method=='POST':
    #    miFormulario = userEditForm(request.POST, request.FILES, instance.usuario)
     #   if miFormulario.is_valid():
      #      if miFormulario.cleaned_data.get ('imagen')
       #         if Imagen.objects.filter(user=usuario).exists():
        #            usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
         #           usuario.imagen.save()
          #          else:
           #             avatar =Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen')
            #            avatar.save()
             #   miFormulario.save()
              #  return render(request, "accounts/base.html")
    #else:
     #   miFormulario = UserEditForm(instance=usuario)
    #return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})

#class CambiarContrasena(loginRequiredMixin, PasswordChangeView):

