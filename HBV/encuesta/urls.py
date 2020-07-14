from django.conf.urls import url,include
from encuesta.views import CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete, PreguntaList, PreguntaDelete, PreguntaCreate, PreguntaUpdate, PreguntaDetail

app_name="encuesta"
urlpatterns = [
	url(r'^nuevo$',CategoriaCreate.as_view(), name='categoria_crear'),
    url(r'^listar$',CategoriaList.as_view(), name='categoria_listar'),
    url(r'^editar/(?P<pk>\d+)/$',CategoriaUpdate.as_view(), name='categoria_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',CategoriaDelete.as_view(), name='categoria_eliminar'),
    url(r'^listar_pre$',PreguntaList.as_view(), name='pregunta_listar'),
    url(r'^nuevo_pre$',PreguntaCreate.as_view(), name='pregunta_crear'),
    url(r'^editar_pre/(?P<pk>\d+)/$',PreguntaUpdate.as_view(), name='pregunta_editar'),
    url(r'^eliminar_pre/(?P<pk>\d+)/$',PreguntaDelete.as_view(), name='pregunta_eliminar'),
    url(r'^detalle_pre/(?P<pk>\d+)/$',PreguntaDetail.as_view(), name='pregunta_detalle'),
]