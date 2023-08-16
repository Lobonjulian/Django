from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=30)
    
    def __str__(self):
        return self.titulo
    
class Articulo(models.Model):
    headline = models.CharField(max_length=100)
    publicacion = models.ManyToManyField(Publicacion)
    
    def __str__(self):
        return self.headline
    