from django.db import models

# Create your models here.
class Categoria(models.Model):
	id_categoria = models.AutoField(primary_key = True)
	descripcion_cat = models.CharField(max_length = 100)
	def __str__(self):
		return '{}'.format(self.descripcion_cat) 
	

	class Meta:
		db_table = 'categoria'


class Departamento(models.Model):
	id_depa = models.AutoField(primary_key = True)
	nombre_depa = models.CharField(max_length = 150)

	class Meta:
		db_table = 'departamento'


class Encuesta(models.Model):
	id_encuesta = models.AutoField(primary_key = True)
	fk_id_departamento = models.ForeignKey("Departamento", on_delete = models.CASCADE)
	fk_id_municipio = models.ForeignKey("Municipio", on_delete = models.CASCADE)
	fecha = models.DateField()
	hora = models.TimeField()

	class Meta:
		db_table = 'encuesta'


class Municipio(models.Model):
	id_municipio = models.AutoField(primary_key = True)
	fk_id_departamento = models.ForeignKey("Departamento", on_delete = models.CASCADE, blank = True, null = True)
	nombre_muni = models.CharField(max_length = 150)

	class Meta:
		db_table = 'municipio'


class Pregunta(models.Model):
	id_pregunta = models.AutoField(primary_key = True)
	fk_id_categoria = models.ForeignKey("Categoria", on_delete = models.CASCADE)
	nombre_pre = models.CharField(max_length = 200)

	class Meta:
		db_table = 'pregunta'


class Respuesta(models.Model):
	id_respuesta = models.AutoField(primary_key = True)
	fk_id_pregunta = models.ForeignKey("Pregunta", on_delete = models.CASCADE)
	fk_id_encuesta = models.ManyToManyField(Encuesta)
	valor = models.IntegerField()

	class Meta:
		db_table = 'respuesta'
