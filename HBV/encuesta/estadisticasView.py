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
				#print(str(c.descripcion_cat) + ",")
				catGragh.append(str(c.descripcion_cat))
			#print(catGragh)
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
				preguntas_cat = Pregunta.objects.filter(fk_id_categoria = id_categoria)	#2(10,11)
				'''print("***************************")
				print(preguntas_cat)
				print("***************************")'''

				'''for pregunta_cat in preguntas_cat:
					id_pregunta = pregunta_cat.id_pregunta
					respuestas_pre_cat = Respuesta.objects.filter(fk_id_pregunta = id_pregunta)
					print("***************************")
					print(respuestas_pre_cat)
					print("***************************")'''

				for enc in encuestas:	#2
					id_encuesta = enc.id_encuesta
					'''respuestas_pre_cat_enc = Respuesta.objects.filter(fk_id_pregunta = id_pregunta, fk_id_encuesta = id_encuesta)
					print("***************************")
					print(respuestas_pre_cat_enc)
					print("***************************")'''

					acumulador_res = 0
					for pre in preguntas_cat:		#2(10,11)
						id_pregunta = pre.id_pregunta 	#2(10
						#respuesta_pre_cat_enc = Respuesta.objects.get(fk_id_pregunta = id_pregunta, fk_id_encuesta = id_encuesta)
						'''print("***************************")
						print(respuesta_pre_cat_enc)
						print("***************************")'''
						#print(respuesta_pre_cat_enc.valor)
						respuestas_pre_cat = Respuesta.objects.filter(fk_id_pregunta = id_pregunta)	#2(1,1)
						for res in respuestas_pre_cat:
							if res.valor == 1:
								#acumulador_res += respuesta_pre_cat_enc.valor
								acumulador_res += 1
							#else:
							#	acumulador_res += 0
					#print("***************************")
					#print(acumulador_res)
				data_main_graph.append(acumulador_res)
				#print(data_main_graph)

		except Exception as e:
			print(e)
		return data_main_graph


	def obtener_num_encuestas(self):
		num_encuestas = Encuesta.objects.all().count()
		#print(num_encuestas)
		return num_encuestas


	def obtener_num_categorias(self):
		num_categorias = Categoria.objects.all().count()
		#print(num_categorias)
		return num_categorias


	def obtener_num_preguntas(self):
		num_preguntas = Pregunta.objects.all().count()
		#print(num_preguntas)
		return num_preguntas


	#Funciones para Gráfico Categoría Economía
	'''
	def obtener_categories_economia_graph(self, categoria_parametro):
		#print(categoria_parametro)
		categories_economia_graph = []
		try:
			id_cat_economia = Categoria.objects.get(descripcion_cat = categoria_parametro)
			#print(id_cat_economia.id_categoria)
			preguntas_cat = Pregunta.objects.filter(fk_id_categoria = id_cat_economia.id_categoria).order_by("id_pregunta")
			#print(preguntas_cat)

			for pre_cat in preguntas_cat:
				id_pre_cat = Pregunta.objects.get(id_pregunta = pre_cat.id_pregunta)
				categories_economia_graph.append(id_pre_cat.nombre_pre) #id_pregunta

			#print(categories_economia_graph)
		except Exception as e:
			print(e)		
		
		return categories_economia_graph


	def obtener_data_economia_graph(self, categoria_parametro):
		data_economia_graph = []
		try:
			id_cat_economia = Categoria.objects.get(descripcion_cat = categoria_parametro)
			#print(id_cat_economia.id_categoria)
			preguntas_cat = Pregunta.objects.filter(fk_id_categoria = id_cat_economia.id_categoria).order_by("id_pregunta")
			#print(preguntas_cat)
			
			for pre in preguntas_cat:
				respuestas_pre_cat = Respuesta.objects.filter(fk_id_pregunta = pre.id_pregunta)
				#print(respuestas_pre_cat)
				acumulador_res = 0
				for res in respuestas_pre_cat:
					if res.valor == 1:
						acumulador_res += 1
				data_economia_graph.append(acumulador_res)
				#print(data_economia_graph)

		except Exception as e:
			print(e)
		return data_economia_graph
	'''


	def obtener_nombre_categoria(self, id_categoria):
		nom_cat = Categoria.objects.get(id_categoria = id_categoria)
		#print(nom_cat.descripcion_cat)
		return nom_cat.descripcion_cat


	def obtener_categories_secondary_graph(self, id_categoria):
		#print(categoria_parametro)
		categories_secondary_graph = []
		try:
			cat = Categoria.objects.get(id_categoria = id_categoria)
			#print(id_cat.id_categoria)
			preguntas_cat = Pregunta.objects.filter(fk_id_categoria = cat.id_categoria).order_by("id_pregunta")
			#print(preguntas_cat)

			for pre_cat in preguntas_cat:
				pre_cat = Pregunta.objects.get(id_pregunta = pre_cat.id_pregunta)
				categories_secondary_graph.append(pre_cat.nombre_pre) #id_pregunta

			#print(categories_economia_graph)
		except Exception as e:
			print(e)		
		
		return categories_secondary_graph


	def obtener_data_secondary_graph(self, id_categoria):
		data_secondary_graph = []
		try:
			cat = Categoria.objects.get(id_categoria = id_categoria)
			#print(id_cat_economia.id_categoria)
			preguntas_cat = Pregunta.objects.filter(fk_id_categoria = cat.id_categoria).order_by("id_pregunta")
			#print(preguntas_cat)
			
			for pre in preguntas_cat:
				respuestas_pre_cat = Respuesta.objects.filter(fk_id_pregunta = pre.id_pregunta)
				#print(respuestas_pre_cat)
				acumulador_res = 0
				for res in respuestas_pre_cat:
					if res.valor == 1:
						acumulador_res += 1
				data_secondary_graph.append(acumulador_res)
				#print(data_economia_graph)

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
		#context['categories_economia_graph'] = self.obtener_categories_economia_graph("Economía")
		#context['data_economia_graph'] = self.obtener_data_economia_graph("Economía")
		#context['categories_escases_graph'] = self.obtener_categories_economia_graph("Escases")
		#context['data_escases_graph'] = self.obtener_data_economia_graph("Escases")
		#context['categories_miedo_graph'] = self.obtener_categories_economia_graph("Miedo a contagiarse")
		#context['data_miedo_graph'] = self.obtener_data_economia_graph("Miedo a contagiarse")
		#context['categories_trabajo_graph'] = self.obtener_categories_economia_graph("Trabajo")
		#context['data_trabajo_graph'] = self.obtener_data_economia_graph("Trabajo")
		#context['categories_transporte_graph'] = self.obtener_categories_economia_graph("Transporte")
		#context['data_transporte_graph'] = self.obtener_data_economia_graph("Transporte")

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
		return context
