from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView
from django.core.urlresolvers import reverse_lazy 
from .models import *
# Create your views here.
class newProducto(CreateView):
    template_name = 'produccion/nuevo_producto.html'
    model = Productos
    fields = ['numero_de_orden','estado_del_producto','comentario']
    success_url = reverse_lazy('nuevo_producto_view')

    def form_valid(self, form):
        form.instance.jefe_de_linea = self.request.user
        return super(newProducto, self).form_valid(form)