# Generated by Django 5.0.6 on 2024-06-30 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0006_producto_tienda_delete_trinket_producto_tienda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tiempo_espera_max',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tiempo_espera_min',
        ),
    ]