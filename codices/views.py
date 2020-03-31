from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponse
from .models import *
from .forms import SignUpForm, DocenteForm, CursoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView



# Create your views here.
#def inicio(request):
#	return render_to_response("Inicio/inicio.html")

def deportes(request):
	deportes_list = Curso.objects.all().filter(categoria = "Deportes")
	context = {'curso_deportes' : deportes_list}
	return render_to_response("Deportes/deportes.html", context)
	
def arte(request):
	arte_list = Curso.objects.all().filter(categoria = "Arte")
	context = {'curso_arte': arte_list}
	return render_to_response("Arte/arte.html", context)

def educacion(request):
	educacion_list = Curso.objects.all().filter(categoria = "Educación")
	context = {'curso_educacion': educacion_list}
	return render_to_response("Educacion/educacion.html", context)

def tecnologia(request):
	tecnologia_list = Curso.objects.all().filter(categoria = "Tecnología")
	context = {'curso_tecnologia': tecnologia_list}
	return render_to_response("Tecnologia/tecnologia.html", context)

def registro_docente(request):
	if request.method == 'POST':
		form = DocenteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = DocenteForm()
	return render(request, 'Registros/RegistroDocente/registro_docente.html', {'form':form})

def inicio_sesion_estudiante(request):
	return render_to_response("IniciarSesion/Estudiante/iniciaSesionEstudiante.html")

def inicio_sesion_docente(request):
	return render_to_response("IniciarSesion/Docente/iniciaSesionDocente.html")


def añadir_curso(request):
	if request.method == 'POST':
		form = CursoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = CursoForm()

	return render(request, 'AñadirCurso/añadir_curso.html', {'form': form})
	
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'Inicio/inicio.html'

class SignInView(LoginView):
    template_name = 'IniciarSesion/Estudiante/iniciaSesionEstudiante.html'

class SignOutView(LogoutView):
    pass

