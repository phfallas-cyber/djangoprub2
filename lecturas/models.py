from django.db import models

# Create your models here.

# ahora voy a crear la tabla para las lecturas
class Caragral(models.Model):
    Abonadoid=models.CharField(max_length=15)
    Nombre=models.CharField(max_length=90)
    Lectura_anterior=models.IntegerField(default=0)
    Lectura_actual=models.IntegerField(default=0)
    Observacion=models.CharField(max_length=150,null=True,blank=True)

    class Meta:
        verbose_name='Caragral'
        verbose_name_plural='caragral'

    def __str__(self):
        
        #return self.Abonadoid
        return str(self.Abonadoid) + " - " + self.Nombre + " - " + str(self.Lectura_actual)