from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Ordenes)
class ordenes_admin(admin.ModelAdmin):
	list_display  = ('id','fecha','cantidad_de_piezas','datos_de_piezas',
		'estado_de_orden','usuario_de_almacen','jefe_de_linea')
	list_filter = ('fecha','estado_de_orden')
