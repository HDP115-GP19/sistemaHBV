"""HBV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from encuesta import views
from encuesta import estadisticasView
from django.contrib.auth.views import login,logout_then_login,password_reset,password_reset_done,password_reset_confirm, password_reset_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    #Urls temporales
    path('entornoAdmin/',include('encuesta.urls',namespace="encuesta")),
    path('entornoUser/', views.entorno_user),
    url(r'^accounts/login/', login, {'template_name':'login.html'}, name='login' ),
    url(r'^logout/', logout_then_login,name='logout'),
    path('estadisticas/', estadisticasView.Estadistica.as_view(), name = "estadisticas"),
    url(r'^reset/password_reset', password_reset, {'template_name':'registration/form.html','email_template_name':'registration/password_reset_email.html'}, name = 'password_reset'),
    url(r'^reset/password_reset_done', password_reset_done, {'template_name':'registration/password_reset_done.html'},name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-94-Za-z_\-]+)/(?P<token>.+)/$',password_reset_confirm,{'template_name':'registration/confirmar.html'},name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name':'registration/resetdone.html'},name='password_reset_complete'),
   


]
