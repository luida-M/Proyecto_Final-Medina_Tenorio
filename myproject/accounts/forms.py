from django import forms
from accounts.models import Desarrollador

class InfDesarrollador(forms.Form):
    desarrollador = forms.CharField() 
    proyecto = forms.CharField() 
    email = forms.EmailField()
    
class BuscaDesarrollador(forms.Form):
    desarrollador = forms.CharField()
    
        
    
    