from django import forms
from django.forms import widgets
from encuesta.models import Departamento, Encuesta, Municipio, Respuesta

class EncuestaForm(forms.ModelForm):
	fk_id_departamento = forms.ModelChoiceField(queryset = Departamento.objects.all().order_by("nombre_depa"), label='Departamento',
		widget = forms.Select(attrs={'class':'form-control'}), empty_label="Seleccione su departamento")

	fk_id_municipio = forms.ModelChoiceField(queryset = Municipio.objects.all().order_by("nombre_muni"), label='Municipio',
		widget = forms.Select(attrs={'class':'form-control'}), empty_label="Seleccione su municipio")

	class Meta:
		model = Encuesta
		fields=[ 'fk_id_departamento',
		'fk_id_municipio',]


class RespuestaForm(forms.ModelForm):
	#fk_id_pregunta = 
	#fk_id_encuesta
	CHOICES = [(1,'Si'), (0,'No')]
	valor = forms.ChoiceField(required=False, widget = forms.CheckboxInput())#choices = CHOICES, 

	class Meta:
		model = Respuesta
		fields = ['valor']