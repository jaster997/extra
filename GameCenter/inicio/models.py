from tabnanny import verbose
from django.db import models

# Create your models here.


class productos(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    nombre= models.CharField(max_length=255, verbose_name="Producto")
    categoria= models.CharField(max_length=255, verbose_name="Categoria")
    precio= models.CharField(max_length=255, verbose_name="Precio")
    existencia= models.CharField(max_length=255, verbose_name="Existencia")
    informacion= models.TextField(verbose_name="Informacion")
    imagen= models.ImageField(null= True, upload_to="fotos", verbose_name="Imagen")
    creacion= models.DateTimeField(auto_now_add=True)
    actualizacion= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "Catalogo"
        verbose_name_plural= "Catalogos"
        ordering= ["-creacion"]

    def __str__(self):
        return self.nombre
        

class comunidad(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    nombre= models.CharField(max_length=50, verbose_name="Usuario")
    producto= models.CharField(max_length=50, verbose_name="Producto")
    mensaje= models.TextField(verbose_name="Mensaje")
    creacion= models.DateField(auto_now_add=True)

    class Meta:
        verbose_name= "Comunidad"
        ordering= ["-creacion"]

    def __str__(self):
        return self.nombre

        
class empresas(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    proveedor= models.CharField(max_length=255, verbose_name="Proveedor")
    sugerencia= models.TextField(max_length=255, verbose_name="Sugerencias")
    archivo= models.FileField(upload_to="archivos", null=True, blank=True)
    creacion= models.DateTimeField(auto_now_add=True)
    actualizacion= models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name= "Sugerencias"
        verbose_name_plural= "Sugerencias"
        ordering= ["-creacion"]

    def __str__(self):
        return self.proveedor

