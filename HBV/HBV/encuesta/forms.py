from django import forms
from encuesta.models import Categoria, Pregunta


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

class PreguntaForm(forms.ModelForm):
	class Meta:
		model = Pregunta

		fields = [
			'nombre_pre',
			'fk_id_categoria',
		]

		labels = {
			'nombre_pre': 'Descripcion de pregunta',
			'fk_id_categoria': 'ID de categoría a la que pertenece',
			}

		widgets = {
			'nombre_pre': forms.TextInput(attrs={'class':'form-control'}),
			'fk_id_categoria': forms.Select(attrs={'class':'form-control'}),
		}