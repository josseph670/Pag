from django.db import models

# Create your models here.
from django.db import models

class Trinket(models.Model):
    OPCIONES_CATEGORIA = [
        (1, '1☆'),
        (2, '2☆'),
        (3, '3☆'),
        (4, '4☆'),
    ]
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    categoria = models.IntegerField(choices=OPCIONES_CATEGORIA)


    def __str__(self):
        return self.nombre