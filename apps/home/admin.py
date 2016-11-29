from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Empleado)
class empleado_admin(admin.ModelAdmin):
	list_display  = ('usuario','nombre','empleado_area','empleado_turno','empleado_puesto')
	list_filter = ('empleado_area','empleado_turno','empleado_puesto')
