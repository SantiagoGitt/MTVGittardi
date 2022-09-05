from django.db import models

class Familia(models.Model):
    nombre= models.CharField(max_length=56)
    apellido= models.CharField(max_length=50)
    Edad= models.IntegerField()
    relacion= models.CharField(max_length=50)
    cumple=models.DateField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.Edad}, {self.relacion}, {self.cumple}"
