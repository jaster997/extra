from django import forms
from .models import comunidad, empresas
from django.forms import ModelForm, ClearableFileInput

class comentarioForm(forms.ModelForm):
    class Meta:
        model= comunidad
        fields= ['nombre', 'producto', 'mensaje']


class archivoInput(ClearableFileInput):
    template_with_clear= '<br><label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class empresasForm(ModelForm):
    class Meta:
        model= empresas
        fields= ('proveedor', 'sugerencia', 'archivo')
        widgets= {
            'archivo': archivoInput
        }