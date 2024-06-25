from django.db import models

# Create your models here.
class Mascota(models.Model):
    id_mascota       = models.CharField(primary_key=True, max_length=10)
    nombre_mascota   = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    raza_mascota     = models.CharField(max_length=20)
    id_sexo          = models.ForeignKey('Sexo',on_delete=models.CASCADE, db_column='idSexo')

    def __str__(self):
        return str(self.nombre_mascota)
       
class Sexo(models.Model):
    id_sexo  = models.AutoField(db_column='idSexo', primary_key=True) 
    sexo     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.sexo)