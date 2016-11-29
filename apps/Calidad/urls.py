from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^jefesdelinea/$',jefes_linea,name='jefes_de_linea'),
	url(r'^ordenes_abiertas/$',ordenes_abiertas,name='ordenes_abiertas'),
	url(r'^detalle_orden/(?P<pk>\d+)$', cambiarEstado.as_view(), name='cambio_estado'),
]