from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Productos)
class productos_admin(admin.ModelAdmin):
	list_display  = ('numero_de_orden','estado_del_producto','comentario','jefe_de_linea')
	list_filter = ('estado_del_producto',)
