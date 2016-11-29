from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy 
from .forms import *

class newOrden(FormView):
    template_name = 'almacen/nuevasordenes.html'
    form_class = OrdenesForm
    success_url = reverse_lazy('nueva_orden')

    def form_valid(self,form):
        orden = Ordenes()
        orden.cantidad_de_piezas = form.cleaned_data['cantidad_de_piezas']
        orden.datos_de_piezas = form.cleaned_data['datos_de_piezas']
        orden.estado_de_orden = 'Abierto'
        orden.usuario_de_almacen = self.request.user
        orden.jefe_de_linea = form.cleaned_data['jefe_de_linea']
        orden.save()
        return super(newOrden, self).form_valid(form)
