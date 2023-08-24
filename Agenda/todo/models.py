from django.db import models
from datetime import date

class Todo(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descripción = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    fecha_fin = models.DateField()
    priority = models.IntegerField(default=3)
    
    def __str__(self):
        return self.titulo
    