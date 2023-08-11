from django.db import models

# Create your models here.
class Name(models.Model):

    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField(null=True)
    signature = models.CharField(max_length=100, default='Firma')
    
    def __str__(self):
        return self.name
    
##