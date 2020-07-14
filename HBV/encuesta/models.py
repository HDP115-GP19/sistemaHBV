from django.db import models

# Create your models here.
class Categoria(models.Model):
	id_categoria = models.AutoField(db_column = 'id_categoria', primary_key = True)
	descripcion_cat = models.CharField(db_column = 'descripcion_cat', max_length = 100)

	class Meta:
		db_table = 'categoria'


	def __str__(self):
		return '{}'.format(self.descripcion_cat)


class Departamento(models.Model):
	id_depa = models.AutoField(db_column = 'id_depa',primary_key = True)
	nombre_depa = models.CharField(db_column = 'nombre_depa',max_length = 150)

	class Meta:
		db_table = 'departamento'


class Encuesta(models.Model):
	id_encuesta = models.AutoField(db_column = 'id_encuesta', primary_key = True)
	fk_id_departamento = models.ForeignKey('Departamento', db_column = 'fk_id_departamento', on_delete = models.CASCADE)
	fk_id_municipio = models.ForeignKey('Municipio', db_column = 'fk_id_municipio', on_delete = models.CASCADE)
	fecha = models.DateField(db_column = 'fecha')
	hora = models.TimeField(db_column = 'hora')

	class Meta:
		db_table = 'encuesta'


class Municipio(models.Model):
	id_municipio = models.AutoField(db_column = 'id_municipio',primary_key = True)
	fk_id_departamento = models.ForeignKey('Departamento', db_column = 'fk_id_departamento', on_delete = models.CASCADE, blank = True, null = True)
	nombre_muni = models.CharField(max_length = 150)

	class Meta:
		db_table = 'municipio'


class Pregunta(models.Model):
	id_pregunta = models.AutoField(db_column = 'id_pregunta', primary_key = True)
	fk_id_categoria = models.ForeignKey('Categoria', db_column = 'fk_id_categoria', on_delete = models.CASCADE)
	nombre_pre = models.CharField(db_column = 'nombre_pre', max_length = 200)

	class Meta:
		db_table = 'pregunta'


	def __str__(self):
		return '{}'.format(str(self.id_pregunta))


class Respuesta(models.Model):
	id_respuesta = models.AutoField(db_column = 'id_respuesta', primary_key = True)
	fk_id_pregunta = models.ForeignKey('Pregunta', db_column = 'fk_id_pregunta', on_delete = models.CASCADE)
	fk_id_encuesta = models.ForeignKey('Encuesta', db_column = 'fk_id_encuesta', on_delete = models.CASCADE, blank = True, null = True)
	valor = models.IntegerField(db_column = 'valor')

	class Meta:
		db_table = 'respuesta'
