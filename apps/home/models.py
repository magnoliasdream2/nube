from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Empleado(models.Model):
	usuario = models.OneToOneField(User,related_name="profile")
	nombre = models.CharField(max_length=64)
	area = (('Automotriz','Automotriz'),('Microtecnologica','Microtecnologica'),('Mixta','Mixta'))
	empleado_area = models.CharField(max_length =20,choices=area)
	turno = (('6:00 AM - 6:00 PM','6:00 AM - 6:00 PM'),('6:00 PM - 6:00 AM','6:00 PM - 6:00 AM'))
	empleado_turno =models.CharField(max_length =20,choices=turno)
	puesto = (('Jefe de linea','Jefe de linea'),('Jefe de calidad','Jefe de calidad'),
		('Almacen','Almacen'),('Gerencia','Gerencia'))
	empleado_puesto =models.CharField(max_length =20,choices=puesto)

	def __unicode__(self):
		return ' %s %s ' %(self.usuario.username , self.empleado_area)


	

	