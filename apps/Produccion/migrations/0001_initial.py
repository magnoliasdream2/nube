# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_del_producto', models.CharField(max_length=15, choices=[(b'Terminado', b'Terminado'), (b'No Terminado', b'No Terminado')])),
                ('comentario', models.CharField(max_length=100)),
                ('jefe_de_linea', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('numero_de_orden', models.ForeignKey(to='Almacen.Ordenes')),
            ],
        ),
    ]
