from django import forms
from accounts.models import FormCliente, Desarrollador

#class InfDesarrollador(forms.Form):
#    desarrollador = forms.CharField() 
#    proyecto = forms.CharField() 
#    email = forms.EmailField()
    

class BuscaDesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = ['nombre']  # Campo por el cual se realizará la búsqueda


#class FormClienteForm(forms.Form):
#    # campos del formulario
#    cliente = forms.CharField(max_length=100)
#    email = forms.EmailField()


class FormClienteForm(forms.ModelForm):
    class Meta:
        model = FormCliente
        fields = ['nombre', 'email']






    

        
    
    