from django import forms
from apps.home.models import *
from .models import *

class OrdenesForm(forms.ModelForm):
	piezas = (('7','7 Piezas'),('16','16 Piezas'))
	cantidad_de_piezas = forms.ChoiceField(choices=piezas)
	datos_de_piezas = forms.CharField(max_length=100)
	#estado = (('Abierto','Abierto'),('Cerrado','Cerrado'))
	#estado_de_orden = forms.ChoiceField(choices=estado)
	jefe_de_linea = forms.ModelChoiceField(queryset=Empleado.objects.filter(empleado_puesto="Jefe de linea"))
	
	class Meta:
		model = Ordenes
		fields = ['cantidad_de_piezas','jefe_de_linea']