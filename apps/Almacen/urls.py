from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^nueva/$',newOrden.as_view(),name='nueva_orden'),
]