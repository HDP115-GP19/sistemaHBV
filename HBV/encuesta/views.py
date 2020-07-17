from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import datetime
# *******************CLASES********************************
from django.urls import reverse_lazy
#libreria para vista de tipo lista de django
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
#*********************************************************
from encuesta.forms import CategoriaForm, PreguntaForm
from encuesta.models import Categoria, Pregunta, Municipio, Departamento, Encuesta, Respuesta
# Create your views here.
#Vistas temporales

def entorno_admin(request):
	return render(request, 'plantillasBase/baseAdmin.html')

def entorno_user(request):
	return render(request, 'plantillasBase/baseUser.html')
	
#******************************************************************************************************
#VISTAS BASADAS EN CLASES PARA GESTIONAR CATEGORIA
class CategoriaList(ListView):
	queryset=Categoria.objects.order_by("id_categoria")
	template_name = 'categoria/categoria_list.html'

class CategoriaCreate(CreateView):
	modelo = Categoria
	form_class = CategoriaForm
	template_name = 'categoria/categoria_form.html'
	success_url = reverse_lazy('encuesta:categoria_listar')


class CategoriaUpdate(UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'categoria/categoria_update.html'
	success_url = reverse_lazy('encuesta:categoria_listar')

class CategoriaDelete(DeleteView):
	model = Categoria
	template_name = 'categoria/categoria_delete.html'
	success_url = reverse_lazy('encuesta:categoria_listar')		
#*******************************************************************************************************
#VISTAS BASADAS EN CLASES PARA GESTIONAR PREGUNTA
class PreguntaList(ListView):
	queryset=Pregunta.objects.order_by("id_pregunta")
	template_name = 'pregunta/pregunta_list.htm'

class PreguntaCreate(CreateView):
	model = Pregunta
	form_class = PreguntaForm
	template_name = 'pregunta/pregunta_form.htm'
	success_url = reverse_lazy('encuesta:pregunta_listar')

class PreguntaUpdate(UpdateView):
	model = Pregunta
	form_class = PreguntaForm
	template_name = 'pregunta/pregunta_update.htm'
	success_url = reverse_lazy('encuesta:pregunta_listar')

class PreguntaDelete(DeleteView):
	model = Pregunta
	template_name = 'pregunta/pregunta_delete.htm'
	success_url = reverse_lazy('encuesta:pregunta_listar')

class PreguntaDetail(DetailView):
	model = Pregunta
	template_name = 'pregunta/pregunta_detail.htm'
	success_url = reverse_lazy('encuesta:pregunta_listar')
#*******************************************************************************************************
def responderEncuesta(request):
	departamentos = Departamento.objects.all()
	categorias = Categoria.objects.all()

	#Si se envía la encuesta
	if request.method == 'POST':
		
		#Se crea una nueva encuesta
		encuesta = Encuesta()
		
		#Se le asignan valores a las variales para el modelo Encuesta
		fecha = datetime.date.today()
		hora = datetime.datetime.now().strftime('%H:%M:%S')
		departamento = Departamento.objects.get(pk=request.POST['departamento'])
		municipio = Municipio.objects.get(pk=request.POST['municipio'])

		#Se le asignan las variables al modelo encuesta
		encuesta.fecha = fecha
		encuesta.hora = hora
		encuesta.fk_id_departamento = departamento
		encuesta.fk_id_municipio = municipio
		
		#Se registra la encuesta
		encuesta.save()

		#Se obtienen las preguntas enviadas desde el template
		preguntas = request.POST.getlist('preguntas')

		for p in preguntas:
			
			#Se crea una nueva respuesta
			respuesta = Respuesta()

			#Asignación de valores a las variables para el modelo Respuesta
			pregunta = Pregunta.objects.get(pk=p)
			valor = request.POST['pregunta'+p]

			#Asignación de variables al modelo Respuesta
			respuesta.valor = valor
			respuesta.fk_id_encuesta = encuesta
			respuesta.fk_id_pregunta = pregunta

			#Se registra la respuesta
			respuesta.save()

		return redirect('estadisticas')

	context = {
		'departamentos' : departamentos,
		'categorias' : categorias,
	}

	return render(request, 'encuesta/responder_encuesta.html', context)

def municipiosPorDepartament(request, id_deparmento):
	municipios = Municipio.objects.filter(fk_id_departamento=id_deparmento)
	#raise Exception("I want to know the value of this: " + municipios)
	
	municipios = Municipio.objects.filter(fk_id_departamento=id_deparmento)
	municipios_list = serializers.serialize('json', municipios)

	return HttpResponse(municipios_list, content_type="text/json-comment-filtered")