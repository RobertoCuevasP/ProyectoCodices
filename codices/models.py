from django.db import models
from smart_selects.db_fields import ChainedManyToManyField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Instructor(models.Model):
	nombre = models.CharField(max_length=100, null=False)
	CI = models.IntegerField()
	ID = models.AutoField(primary_key=True)
	email = models.EmailField()
	telefono = models.IntegerField()
	password = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.nombre

class Curso(models.Model):
	DEPORTES = 'Deportes'
	TECNOLOGIA = 'Tecnología'
	ARTE = 'Arte'
	EDUCACION = 'Educación'
	CATEGORIA_CHOICES = (
		(DEPORTES, u'Deportes'),
		(TECNOLOGIA, u'Tecnología'),
		(ARTE, u'Arte'),
		(EDUCACION, u'Educación'),
	)

	PRESENCIAL = 'Presencial'
	VIRTUAL = 'Virtual'
	MODALIDAD_CHOICES = (
		(PRESENCIAL, u'Presencial'),
		(VIRTUAL, u'Virtual'),
	)

	ID = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, blank = False)
	costo = models.CharField(max_length=10)
	tipo = models.CharField(max_length=10, choices=MODALIDAD_CHOICES, blank = False)
	descripcion = models.CharField(max_length=1000)
	#ubicacion
	fechaInicio = models.DateField()
	fechaFin = models.DateField()
	imagen = models.ImageField(upload_to = 'cursos/')

	def __str__(self):
		return self.nombre


class Perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	ID = models.AutoField(primary_key=True)
	def __str__(self):
		return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()

class Supervisor(models.Model):
	nombre = models.CharField(primary_key = True, max_length=100)
	email = models.EmailField()
	telefono = models.IntegerField()
	def __str__(self):
		return self.nombre
