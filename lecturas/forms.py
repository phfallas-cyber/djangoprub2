from django import forms
from .models import Caragral



class Formulario(forms.ModelForm):
    class Meta:
        model = Caragral
        fields = '__all__' #  esto muestra todos los campos de la tabla o modelo
        #fields= ['Abonadoid', 'Nombre', 'Lectura_anterior', 'Lectura_actual','Observacion']
        #widgets=[]
        



