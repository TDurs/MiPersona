from django import forms
from .models import Documento, Universidad, Contacto

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'pdf', 'universidad']

        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'gmail', 'interes']