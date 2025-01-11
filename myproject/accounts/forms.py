from django import forms
from accounts.models import Desarrollador

class InfDesarrollador(forms.Form):
    desarrollador = forms.CharField() #label='Nombre del desarrollador', max_length=100)
    proyecto = forms.CharField() #label='Nombre del proyecto', max_length=100)
    email = forms.EmailField()# label='Correo electrónico')
    
class BuscaDesarrollador(forms.Form):
    desarrollador = forms.CharField()
        
    
    