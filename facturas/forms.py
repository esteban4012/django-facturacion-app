from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'})
        }
