from django.db import models

# Create your models here.

class Corte(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    corte = models.ForeignKey(Corte, on_delete=models.PROTECT)
    fecha_reserva = models.DateField()

    def __str__(self):
        return self.nombre
