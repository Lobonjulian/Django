from django.db import models

# Salario
class Salary(models.Model):
    amount = models.IntegerField(null=False)
    ext_dec = models.BooleanField(default=False)
    ext_jun = models.BooleanField(default=False)
    
    def __str__(self):
        self.amount

# Trabajo
class Job(models.Model):
    title = models.CharField(max_length=15, blank=False ,null=False)
    description = models.TextField(null=False)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    
    def __str__(self):
        self.title

# Pais
class Country(models.Model):
    name = models.CharField(max_length=30, blank=False ,null=False)
    country_code = models.CharField(max_length=10, blank=False ,null=False)
    
    def __str__(self):
        self.name

# Localizacion        
class Localition(models.Model):
    name = models.CharField(max_length=30, blank=False ,null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        self.name

# Lugar
class Place(models.Model):
    name = models.CharField(max_length=30, blank=False ,null=False)
    address = models.CharField(max_length=30, blank=False ,null=False)
    zip_code = models.CharField(max_length=10, blank=False ,null=False)
    localizacion = models.ForeignKey(Localition, on_delete=models.CASCADE) 
    
    def __str__(self):
        self.name
        
# Empleado 
class Employes(models.Model):
    id_number = models.CharField(max_length=10, blank=False ,null=False)
    name = models.CharField(max_length=30, blank=False ,null=False)
    last_name = models.CharField(max_length=30, blank=False ,null=False)
    email = models.EmailField(max_length=30, blank=False ,null=False)
    address = models.CharField(max_length=30, blank=False ,null=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    
    def __str__(self):
        self.name