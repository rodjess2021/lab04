from django.db import models

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)

class Candidato(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
