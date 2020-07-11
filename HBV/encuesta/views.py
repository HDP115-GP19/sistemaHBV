from django.shortcuts import render

# Create your views here.

#Vistas temporales
def entorno_admin(request):
	return render(request, 'plantillasBase/baseAdmin.html')

def entorno_user(request):
	return render(request, 'plantillasBase/baseUser.html')