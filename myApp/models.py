from django.db import models

# Create your models here.
class Sensor(models.Model):
    # Nombre del sensor
    nombre = models.CharField(max_length=100)
    
