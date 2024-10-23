from django import forms
from .models import Estudio, Proyecto, Contacto, Perfil

class EstudioForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Acepta el formato DD/MM/YYYY
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/YYYY'})
    )
    fecha_fin = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Acepta el formato DD/MM/YYYY
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/YYYY'})
    )

    class Meta:
        model = Estudio
        fields = ['tipo', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'imagen']


class ProyectoForm(forms.ModelForm):
    fecha_realizacion = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/YYYY'})
    )

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_realizacion', 'url_proyecto', 'imagen']


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto  # Cambia esto por el modelo correcto
        fields = ['nombre', 'email', 'mensaje']  # Asegúrate de que estos sean los campos correctos


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre_completo', 'bio', 'foto_perfil', 'linkedin', 'github']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
        }