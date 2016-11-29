from django import forms
from apps.home.models import *
from apps.Almacen.models import *

class FechaForm(forms.ModelForm):
	fecha = forms.DateTimeField()
	class Meta:
		model = Ordenes
		exclude = ['numero_de_orden','cantidad_de_piezas','datos_de_piezas','estado_de_orden','jefe_de_linea','usuario_de_almacen']
