from django import forms
from encuesta.models import Categoria


#FORMULARIO PARA CREAR CATEGORIA
class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria

		fields = [
			'descripcion_cat',
		]

		labels = {
			'descripcion_cat': 'Descripcion de categoria',
			}

		widgets = {
			'descripcion_cat': forms.TextInput(attrs={'class':'form-control'}),
		}