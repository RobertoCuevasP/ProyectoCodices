from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from .models import Supervisor
admin.site.register(Supervisor)

from .models import Curso
admin.site.register(Curso)

from .models import Instructor
admin.site.register(Instructor)


from .models import Perfil
admin.site.register(Perfil)
 