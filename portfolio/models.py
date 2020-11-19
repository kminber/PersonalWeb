from django.db import models

# Create your models here.
class Project(models.Model):
    tittle = models.CharField(max_length=200, verbose_name="Título")                    #Campo de carácteres
    description = models.TextField(verbose_name="Descripción")                          #Campo de texto 
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")              #Campo de imagen
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") #Campo de fecha donde se añade la hora automáticamente al crearse 
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")      #Campo de fecha donde se añade la hora automáticamente siempre
    link = models.URLField(verbose_name = "Dirección web", null=True, blank=True)

    class Meta: #Clase de metadatos
        verbose_name = "proyecto"           #Asignar nombre en singular
        verbose_name_plural = "proyectos"   #Asignar nombre en plural
        ordering = ["-created"]             #Campo de odenación por defecto mediante fecha de creación

    def __str__(self):
        return self.tittle

