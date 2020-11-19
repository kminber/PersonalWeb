from django.db import models

# Create your models here.
class Project(models.Model):
    tittle = models.CharField(max_length=200)            #Campo de carácteres
    description = models.TextField()                     #Campo de texto 
    image = models.ImageField()                          #Campo de imagen
    created = models.DateTimeField(auto_now_add=True)    #Campo de fecha donde se añade la hora automáticamente al crearse 
    updated = models.DateTimeField(auto_now=True)        #Campo de fecha donde se añade la hora automáticamente siempre
