from django.shortcuts import render
from django.views.generic import ListView
from apps.home.models import *
from apps.Almacen.models import *
from apps.Produccion.models import *
from .forms import *
# Create your views here.
def todos_los_empleados(request):
    empleado_list = Empleado.objects.all()
    empleado_ctx = {'empleados': empleado_list}
    return render(request, 'gerencia/todoelpersonal.html', empleado_ctx)
    
def todos_las_ordenes(request):
    orden_list = Ordenes.objects.all()
    orden_ctx = {'orden': orden_list}
    return render(request, 'gerencia/estado_ordenes.html', orden_ctx)

def todos_los_productos(request):
    producto_list = Productos.objects.all()
    producto_ctx = {'producto': producto_list}
    return render(request, 'gerencia/estado_productos.html', producto_ctx)



def reportes(request):
    form = FechaForm()
    obj = Ordenes.objects.all()
    ctx={'mensaje':obj,'form':form} #muestra todos los objetos
        
    if request.method == "POST":
        form =  FechaForm(request.POST)
        if form.is_valid():
                        
            fecha = form.cleaned_data['fecha'] #obtiene el valor seleccionado
            obj = Ordenes.objects.filter(fecha=fecha) #filtra por el valor seleccionado
            
            ctx={'mensaje':obj,'form':form}
            return render(request, 'gerencia/orden_fecha.html',ctx)
        else:
            form =  FechaForm()

    return render(request, 'gerencia/orden_fecha.html',ctx)
   
