# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('cantidad_de_piezas', models.CharField(max_length=10, choices=[(b'7', b'7 Piezas'), (b'16', b'16 Piezas')])),
                ('datos_de_piezas', models.CharField(max_length=100)),
                ('estado_de_orden', models.CharField(max_length=10, choices=[(b'Abierto', b'Abierto'), (b'Cerrado', b'Cerrado')])),
                ('jefe_de_linea', models.CharField(max_length=20)),
                ('usuario_de_almacen', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
