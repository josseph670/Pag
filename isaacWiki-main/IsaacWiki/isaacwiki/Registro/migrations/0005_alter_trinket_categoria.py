# Generated by Django 4.2.1 on 2023-06-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_alter_trinket_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trinket',
            name='categoria',
            field=models.IntegerField(choices=[(1, '1☆'), (2, '2☆'), (3, '3☆'), (4, '4☆')]),
        ),
    ]
