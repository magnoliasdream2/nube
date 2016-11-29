from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView,ListView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy 
from .models import *
from .forms import *
# Create your views here.
class Welcome_View(TemplateView):
	template_name = 'index.html'

class newEmpleado(FormView):
    template_name = 'test.html'
    form_class = UserForm
    success_url = reverse_lazy('nuevo_empleado')

    def form_valid(self,form):
        user = form.save()
        perfil = Empleado()
        perfil.usuario = user
        perfil.nombre = form.cleaned_data['nombre']
        perfil.empleado_area = form.cleaned_data['empleado_area']
        perfil.empleado_turno = form.cleaned_data['empleado_turno']
        perfil.empleado_puesto = form.cleaned_data['empleado_puesto']
        perfil.save()
        return super(newEmpleado, self).form_valid(form)
