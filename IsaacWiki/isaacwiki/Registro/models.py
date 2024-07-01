from django.db import models

class Tienda(models.Model):
    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=7, choices=ESTADO_CHOICES, default='cerrado')
    tiempo_espera_min = models.IntegerField()
    tiempo_espera_max = models.IntegerField()
    imagen = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField() 
    tienda = models.ForeignKey(Tienda, related_name='productos', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.nombre
    
    def precio_en_pesos(self):
        return "${:,.0f}".format(self.precio)

