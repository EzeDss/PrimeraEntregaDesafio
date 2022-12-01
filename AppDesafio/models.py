from django.db import models

# Create your models here.

class Productos(models.Model):
    producto=models.CharField(max_length=40)
    precio=models.IntegerField()
    stock=models.IntegerField()

class Categorias(models.Model):
    categoria=models.CharField(max_length=40)
    subcategoria=models.CharField(max_length=40)

class Vendedores(models.Model):
    nombre=models.CharField(max_length=40)
    cantidadProductos=models.IntegerField()
    fecha_ingreso=models.DateField()
    mail = models.EmailField(max_length=200, blank=True, null=True)