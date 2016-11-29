from django.db import models
from django.contrib.auth.models import User
from apps.Almacen.models import *
# Create your models here.
class Productos(models.Model):
	numero_de_orden = models.ForeignKey(Ordenes)
	estado = (('Terminado','Terminado'),('No Terminado','No Terminado'))
	estado_del_producto = models.CharField(max_length=15,choices=estado)
	comentario = models.CharField(max_length=100)
	jefe_de_linea  = models.ForeignKey(User)

	def __unicode__(self):
		return self.estado_del_producto
