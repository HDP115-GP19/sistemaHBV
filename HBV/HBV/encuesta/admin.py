from django.contrib import admin
from encuesta import models

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "descripcion_cat")

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("id_depa", "nombre_depa")

class EncuestaAdmin(admin.ModelAdmin):
    list_display = ("id_encuesta", "fk_id_departamento", "fk_id_municipio", "fecha", "hora")
    date_hierarchy = "fecha"

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("id_municipio", "fk_id_departamento", "nombre_muni")

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("id_pregunta", "fk_id_categoria", "nombre_pre")

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ("id_respuesta", "fk_id_pregunta", "valor")
    
admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Departamento, DepartamentoAdmin)
admin.site.register(models.Encuesta, EncuestaAdmin)
admin.site.register(models.Municipio, MunicipioAdmin)
admin.site.register(models.Pregunta, PreguntaAdmin)
admin.site.register(models.Respuesta, RespuestaAdmin)