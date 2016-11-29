from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^empleados/$',todos_los_empleados,name='todos_los_empleados_view'),
	url(r'^estado_ordenes/$',todos_las_ordenes,name='todos_las_ordenes_view'),
	url(r'^estado_producto/$',todos_los_productos,name='todos_los_productos_view'),
	url(r'^orden_fecha/$', reportes, name='reporte'),
]