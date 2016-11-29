from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^$',Welcome_View.as_view(),name='Welcome_View'),
	url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^nuevoEmpleado/$',newEmpleado.as_view(),name='nuevo_empleado'),
]