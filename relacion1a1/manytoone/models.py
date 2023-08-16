from django.db import models

class Reportero(models.Model):
    primer_nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=80)
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
class Articulo(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reportero =models.ForeignKey(Reportero, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline
    