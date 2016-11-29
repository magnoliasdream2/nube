from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^nuevo/$',newProducto.as_view(),name='nuevo_producto_view'),
]