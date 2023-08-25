from django.db import models

class Carrito(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    tipoDePrenda=models.CharField(default='' , max_length=40)
    
# Create your models here.
