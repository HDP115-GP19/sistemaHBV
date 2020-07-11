from django.shortcuts import render, redirect
from django.http import HttpResponse
# *******************CLASES********************************
from django.urls import reverse_lazy
#libreria para vista de tipo lista de django
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#*********************************************************
from encuesta.forms import CategoriaForm
from encuesta.models import Categoria
# Create your views here.

#Vistas temporales

def entorno_admin(request):
	return render(request, 'plantillasBase/baseAdmin.html')

def entorno_user(request):
	return render(request, 'plantillasBase/baseUser.html')
	
#******************************************************************************************************
#VISTAS BASADAS EN CLASES PARA GESTIONAR CATEGORIA
class CategoriaList(ListView):
	model = Categoria
	template_name = 'categoria/categoria_list.html'

class CategoriaCreate(CreateView):
	modelo = Categoria
	form_class = CategoriaForm
	template_name = 'categoria/categoria_form.html'
	success_url = reverse_lazy('categoria:categoria_listar')


class CategoriaUpdate(UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'categoria/categoria_update.html'
	success_url = reverse_lazy('categoria:categoria_listar')

class CategoriaDelete(DeleteView):
	model = Categoria
	template_name = 'categoria/categoria_delete.html'
	success_url = reverse_lazy('categoria:categoria_listar')		
#*******************************************************************************************************		