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
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('empleado_area', models.CharField(max_length=20, choices=[(b'Automotriz', b'Automotriz'), (b'Microtecnologica', b'Microtecnologica'), (b'Mixta', b'Mixta')])),
                ('empleado_turno', models.CharField(max_length=20, choices=[(b'6:00 AM - 6:00 PM', b'6:00 AM - 6:00 PM'), (b'6:00 PM - 6:00 AM', b'6:00 PM - 6:00 AM')])),
                ('empleado_puesto', models.CharField(max_length=20, choices=[(b'Jefe de linea', b'Jefe de linea'), (b'Jefe de calidad', b'Jefe de calidad'), (b'Almacen', b'Almacen'), (b'Gerencia', b'Gerencia')])),
                ('usuario', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
