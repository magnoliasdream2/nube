from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ordenes(models.Model):
	fecha = models.DateField(auto_now=True)
	piezas = (('7','7 Piezas'),('16','16 Piezas'))
	cantidad_de_piezas = models.CharField(max_length=10,choices=piezas)
	datos_de_piezas = models.CharField(max_length=100)
	estado = (('Abierto','Abierto'),('Cerrado','Cerrado'))
	estado_de_orden = models.CharField(max_length=10,choices=estado)
	usuario_de_almacen  = models.ForeignKey(User)
	jefe_de_linea = models.CharField(max_length=20)

	def __unicode__(self):
		return ' %d ' %(self.id)
