from django.views.generic import TemplateView
from encuesta.models import Categoria, Encuesta, Respuesta, Pregunta
from django.db.models import Count
from django.db.models.functions import Coalesce


class Estadistica(TemplateView):
	template_name = 'estadisticas/estadisticas.html'

	#Funciones para Gráfico Principal
	def obtener_categorias_main_graph(self):
		catGragh = []
		try:
			categorias = Categoria.objects.all()
			for c in categorias:
				catGragh.append(c.descripcion_cat)
		except Exception as e:
			print(e)
		return catGragh


	def obtener_data_main_graph(self):
		data_main_graph = []
		try:
			encuestas = Encuesta.objects.all()
			categorias = Categoria.objects.all()

			for cat in categorias:
				id_categoria = cat.id_categoria
				preguntas_cat = Pregunta.objects.filter(fk_id_categoria = id_categoria)

				for enc in encuestas:
					id_encuesta = enc.id_encuesta

					acumulador_res = 0
					for pre in preguntas_cat:
						id_pregunta = pre.id_pregunta
						respuestas_pre_cat = Respuesta.objects.filter(fk_id_pregunta = id_pregunta)	#2(1,1)
						for res in respuestas_pre_cat:
							if res.valor == 1:
								acumulador_res += 1
				data_main_graph.append(acumulador_res)

		except Exception as e:
			print(e)
		return data_main_graph


	def obtener_num_encuestas(self):
		num_encuestas = Encuesta.objects.all().count()
		return num_encuestas


	def obtener_num_categorias(self):
		num_categorias = Categoria.objects.all().count()
		return num_categorias


	def obtener_num_preguntas(self):
		num_preguntas = Pregunta.objects.all().count()
		return num_preguntas


	def obtener_nombre_categoria(self, id_categoria):
		nom_cat = Categoria.objects.get(id_categoria = id_categoria)
		return nom_cat.descripcion_cat


	def obtener_categories_secondary_graph(self, id_categoria):
		categories_secondary_graph = []
		try:
			cat = Categoria.objects.get(id_categoria = id_categoria)
			preguntas_cat = Pregunta.objects.filter(fk_id_categoria = cat.id_categoria).order_by("id_pregunta")

			for pre_cat in preguntas_cat:
				pre_cat = Pregunta.objects.get(id_pregunta = pre_cat.id_pregunta)
				categories_secondary_graph.append(pre_cat.nombre_pre)

		except Exception as e:
			print(e)		
		
		return categories_secondary_graph


	def obtener_data_secondary_graph(self, id_categoria):
		data_secondary_graph = []
		try:
			cat = Categoria.objects.get(id_categoria = id_categoria)
			preguntas_cat = Pregunta.objects.filter(fk_id_categoria = cat.id_categoria)
			
			for pre in preguntas_cat:
				respuestas_pre_cat = Respuesta.objects.filter(fk_id_pregunta = pre.id_pregunta)
				acumulador_res = 0
				for res in respuestas_pre_cat:
					if res.valor == 1:
						acumulador_res += 1
				data_secondary_graph.append(acumulador_res)

		except Exception as e:
			print(e)
		return data_secondary_graph



	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['categorias'] = self.obtener_categorias_main_graph()
		context['data_main_graph'] = self.obtener_data_main_graph()
		context['encuestas_procesadas'] = self.obtener_num_encuestas()
		context['cantidad_categorias'] = self.obtener_num_categorias()
		context['cantidad_preguntas'] = self.obtener_num_preguntas()

		context['nombre_categoria_uno'] = self.obtener_nombre_categoria("1")
		context['categories_uno_graph'] = self.obtener_categories_secondary_graph("1")
		context['data_uno_graph'] = self.obtener_data_secondary_graph("1")

		context['nombre_categoria_dos'] = self.obtener_nombre_categoria("2")
		context['categories_dos_graph'] = self.obtener_categories_secondary_graph("2")
		context['data_dos_graph'] = self.obtener_data_secondary_graph("2")

		context['nombre_categoria_tres'] = self.obtener_nombre_categoria("3")
		context['categories_tres_graph'] = self.obtener_categories_secondary_graph("3")
		context['data_tres_graph'] = self.obtener_data_secondary_graph("3")

		context['nombre_categoria_cuatro'] = self.obtener_nombre_categoria("4")
		context['categories_cuatro_graph'] = self.obtener_categories_secondary_graph("4")
		context['data_cuatro_graph'] = self.obtener_data_secondary_graph("4")

		context['nombre_categoria_cinco'] = self.obtener_nombre_categoria("5")
		context['categories_cinco_graph'] = self.obtener_categories_secondary_graph("5")
		context['data_cinco_graph'] = self.obtener_data_secondary_graph("5")

		context['nombre_categoria_seis'] = self.obtener_nombre_categoria("6")
		context['categories_seis_graph'] = self.obtener_categories_secondary_graph("6")
		context['data_seis_graph'] = self.obtener_data_secondary_graph("6")
		return context
