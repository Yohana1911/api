from django.db import models

# Create your models here.
class API(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)