from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserRegisterForm

# Create your views here.
def login_request(request):
    msg_login= ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('pasword')
            user = authenticate(username=usuario, password=contraseña )
            if user is not None:
                login( request, user)
                return render(request, "accounts/base.html")
        msg_login = "Usuario o contraseña incorrecta"
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})            


def register(request):
    msg_register = ""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "accounts/base.html")
        msg_register = "Error en los datos ingresados"
    form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form, "msg_register": msg_register})        


