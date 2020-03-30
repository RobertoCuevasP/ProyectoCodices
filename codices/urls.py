from django.urls import path
from django.conf.urls import url 
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('deportes/', views.deportes, name='deportes'),
    path('arte/', views.arte, name='arte'),
    path('educacion/', views.educacion, name='educacion'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('registro_docente/', views.registro_docente, name='registro_docente'),
    path('inicio_sesion_docente/', views.inicio_sesion_docente, name='inicio_sesion_docente'),
    path('añadir_curso/', views.añadir_curso, name ='añadir_curso'),
]
