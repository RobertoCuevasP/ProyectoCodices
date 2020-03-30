from django import forms
from .models import Instructor, Curso, Perfil
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.safestring import mark_safe
from django.forms import ImageField
from django.contrib.auth.models import User

class PictureWidget(forms.widgets.Widget):
	def render(self, name, value, attrs=None):
		html = Template("""<img src="$link"/>""")
		return mark_safe(html.substitute(link=value))

class DocenteForm(forms.ModelForm):
	class Meta:
		model =  Instructor

		fields = [
			'nombre',
			'CI',
			'email',
			'telefono',
			'password',
		]

		labels = {
			'nombre': 'Nombre',
			'CI': 'Carnet de Identidad',
			'email': 'Correo Electrónico',
			'telefono': 'Número de Teléfono o Celular',
			'password': 'Contraseña'
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}), 
			'CI':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':	forms.TextInput(attrs={'class':'form-control'}),
			'password' : forms.PasswordInput(),
		}


class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		#imagen = ImageField(widget=PictureWidget)
		fields = [
			'nombre', 
			'categoria',
			'costo',
			'tipo',
			'descripcion',
			'fechaInicio',
			'fechaFin',
			'imagen',
		]

		labels = {
			'nombre': 'Nombre del Curso', 
			'categoria': 'Categoría',
			'costo': 'Costo',
			'tipo':'Modalidad de Clases',
			'descripcion': 'Descripción del Curso',
			'fechaInicio': 'Fecha de Inicio (Formato Año-Mes-Día)',
			'fechaFin': 'Fecha de Finalización (Formato Año-Mes-Día)',
			'imagen': 'Imagen',
		}

		widgets = {
	#		'nombre':forms.TextInput(attrs={'class':'form-control'}), 
	#		'categoria':forms.Select(attrs={'class': 'form-control'}),
	#		'costo':forms.TextInput(attrs={'class':'form-control'}),
	#		'tipo': forms.Select(attrs={'class':'form-control'}),
	#		'descripcion':forms.TextInput(attrs={'class':'form-control'}),
	#		'fechaInicio':forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
	#		'fechaFin':forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
	#		
		}

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
