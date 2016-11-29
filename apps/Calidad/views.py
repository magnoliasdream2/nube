from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy 
from apps.home.models import *
from apps.Almacen.models import *
# Create your views here.
def jefes_linea(request):
    empleado_list = Empleado.objects.filter(empleado_puesto="Jefe de linea")
    empleado_ctx = {'empleados': empleado_list}
    return render(request, 'calidad/jefesdelinea.html', empleado_ctx)

def ordenes_abiertas(request):
    orden_list = Ordenes.objects.all()
    orden_ctx = {'orden': orden_list}
    return render(request, 'calidad/ordenes_abiertas.html', orden_ctx)

class cambiarEstado(UpdateView):
    model = Ordenes
    fields =  ['estado_de_orden']
    template_name = 'calidad/detalle_orden.html'
    success_url = reverse_lazy('ordenes_abiertas')