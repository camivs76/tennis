from django.db import models


    
# Create your models here.
class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True, db_column='id')
    descripcion=models.IntegerField(verbose_name="DNI")
    costo= models.CharField(max_length=50,verbose_name="Nombre y Apellido")
          
    
    def __str__(self):
        fila=str(self.idServicio)+"-"+self.descripcion+"-"+str(self.costo)
        return fila
    
    
# Create your models here.
class Contratacion(models.Model):
    idContratacion = models.AutoField(primary_key=True, db_column='idContratación')
    fecha=models.IntegerField(verbose_name="fecha")
    idServicio= models.ForeignKey(Servicio,verbose_name="idServicio")
    nomContaratante=models.CharField(max_length=25,verbose_name="nomContratante")
    
       
    def __str__(self):
        fila=str(self.idServicio)+"-"+self.fecha+"-"+str(self.idServicio)
        return fila
    

    