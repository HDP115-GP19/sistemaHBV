from django.shortcuts import render, redirect
from django.http import HttpResponse
# *******************CLASES********************************
from django.urls import reverse_lazy
#libreria para vista de tipo lista de django
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
#*********************************************************
from encuesta.forms import CategoriaForm, PreguntaForm
from encuesta.models import Categoria, Pregunta
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