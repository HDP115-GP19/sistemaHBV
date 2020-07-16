from django.conf.urls import url,include
from encuesta.views import CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete, PreguntaList, PreguntaDelete, PreguntaCreate, PreguntaUpdate, PreguntaDetail, municipiosPorDepartament, responderEncuesta
from django.contrib.auth.decorators import login_required
from django.urls import path

app_name="encuesta"
urlpatterns = [
    url(r'^nuevo$',login_required(CategoriaCreate.as_view()), name='categoria_crear'),
    url(r'^listar$',login_required(CategoriaList.as_view()), name='categoria_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(CategoriaUpdate.as_view()) ,name='categoria_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',login_required(CategoriaDelete.as_view()), name='categoria_eliminar'),
    url(r'^listar_pre$',login_required(PreguntaList.as_view()), name='pregunta_listar'),
    url(r'^nuevo_pre$',login_required(PreguntaCreate.as_view()), name='pregunta_crear'),
    url(r'^editar_pre/(?P<pk>\d+)/$',login_required(PreguntaUpdate.as_view()), name='pregunta_editar'),
    url(r'^eliminar_pre/(?P<pk>\d+)/$',login_required(PreguntaDelete.as_view()), name='pregunta_eliminar'),
    url(r'^detalle_pre/(?P<pk>\d+)/$',login_required(PreguntaDetail.as_view()), name='pregunta_detalle'),
    path('responder-encuesta/', responderEncuesta, name='responder_encuesta'),
    path('municipios/<id_deparmento>/', municipiosPorDepartament, name='municipios'),
]