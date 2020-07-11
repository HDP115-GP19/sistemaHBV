from django.conf.urls import url,include
from encuesta.views import CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete

app_name="categoria"
urlpatterns = [
	url(r'^nuevo$',CategoriaCreate.as_view(), name='categoria_crear'),
    url(r'^listar$',CategoriaList.as_view(), name='categoria_listar'),
    url(r'^editar/(?P<pk>\d+)/$',CategoriaUpdate.as_view(), name='categoria_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',CategoriaDelete.as_view(), name='categoria_eliminar'),
]