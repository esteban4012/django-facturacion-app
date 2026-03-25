from django import forms 
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono']


from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el correo'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el telefono'}),
        }