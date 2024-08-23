from django.db import models
from jugadores.models import Jugador

class Organizador(models.Model):
    idOrganizador=models.AutoField(primary_key=True,verbose_name="idOrganizador",db_column='idOrganizador')
    nom=models.CharField(verbose_name="nombre")
    contacto=models.IntegerField(verbose_name="contacto")
    
    def __str__(self):
        fila=str(self.idOrganizador)+"-"+self.nom+""+str(self.contacto)
        return fila
    
        
class Evento(models.Model):
    idEvento=models.AutoField(primary_key=True,verbose_name="idEvento",db_column='idEvento')
    nom= models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fecha=models.DateField(verbose_name="Fecha de Evento")
    ubicacion=models.FloatField(max_length=10,verbose_name="Ubicacion")
    idOrganizacion=models.ForeignKey(Organizador,verbose_name="idOrganizador", on_delete=models.CASCADE)
    
    def __str__(self):
        fila=str(self.idEvento)+"-"+self.nom+""+str(self.idOrganizacion)
        return fila
    
    
    
    
    
    
