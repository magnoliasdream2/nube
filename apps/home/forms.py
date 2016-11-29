from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	nombre = forms.CharField()
	area = (('Automotriz','Automotriz'),('Microtecnologica','Microtecnologica'),('Mixta','Mixta'))
	empleado_area = forms.ChoiceField(choices=area)
	turno = (('6:00 AM - 6:00 PM','6:00 AM - 6:00 PM'),('6:00 PM - 6:00 AM','6:00 PM - 6:00 AM'))
	empleado_turno =forms.ChoiceField(choices=turno)
	puesto = (('Jefe de linea','Jefe de linea'),('Jefe de calidad','Jefe de calidad'),('Almacen','Almacen'),('Gerencia','Gerencia'))
	empleado_puesto =forms.ChoiceField(choices=puesto)