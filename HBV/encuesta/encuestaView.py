from django.views.generic import TemplateView, CreateView
from encuesta.models import Encuesta, Departamento, Pregunta, Categoria, Respuesta
from encuesta.encuestaForm import EncuestaForm, RespuestaForm
from django.urls import reverse_lazy
from datetime import datetime
from django.http import HttpResponseRedirect


class Encuesta(CreateView):
	model = Encuesta
	form_class = EncuestaForm
	second_form_class = RespuestaForm
	template_name = 'encuesta/encuesta.html'
	success_url = reverse_lazy('estadisticas')


	def obtener_preguntas(self):
		preguntas = Pregunta.objects.all()
		#print(preguntas)
		return preguntas


	def obtener_categorias(self):
		categorias = Categoria.objects.all()
		#print(categorias)
		return categorias


	def get_context_data(self, **kwards):
		context = super(Encuesta, self).get_context_data(**kwards)
		context['preguntas'] = self.obtener_preguntas()
		context['categorias'] = self.obtener_categorias()
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context


	def obtener_ult_encuesta(self):
			encuesta = Encuesta.objects.all().last()
			return encuesta


	def post(self,request,*args,**kwards):
		self.object = self.get_object
		form = self.form_class(request.POST)
		#print(form)
		#print("**************************************")
		form2 = self.second_form_class(request.POST)
		#print(form2)
		if form.is_valid() and form2.is_valid():
			print("ENTRO")
			enc_depa_muni = form.save()#save(commit = False)
			respuesta_enc = form2.save(commit = False)
			#encuestaa = self.obtener_ult_encuesta()

			respuestaa = Respuesta()
			respuestaa.fk_id_pregunta = request.POST['id_valor_0']
			respuesta.fk_id_encuesta = enc_depa_muni.id_encuesta#encuestaa.id_encuesta
			
			'''respuesta = Respuesta()
			respuesta.fk_id_pregunta.id_pregunta = request.POST['3']
			respuesta.fk_id_respuesta.id_encuesta = 1#request.POST['3']
			respuesta.valor = request.POST['3']'''
			#respuestam.fk_id_encuesta.id_encuesta = request.POST['1']#encuesta.id_encuesta
			#respuesta = form2.save(commit = False)
			#encuesta.save()
			print("**************************************")
			print(respuesta)
			print("**************************************")
			respuesta_enc.save()
			respuesta.save()

			return HttpResponseRedirect(self.get_success_url())
		else:
			print("NO ENTRO")
			return self.render_to_response(self.get_context_data(form = form, form2 = form2))