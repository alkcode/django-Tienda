from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tel=models.CharField(max_length=10)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.FloatField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
