from socket import fromshare
from django import forms 
from .models import Evento


class EventoForm(forms.ModelForm):
  class Meta:
        model=Evento
       #fields='__all__'
        fields=('idEvento','nom','fecha','ubicacion',"idOrganizacion")
        labels ={
          
            "idEvento":" id Evento",
            'nom': 'nombre y apellido del jugador:',
            "fecha":"Fecha Evento",
            "ubicacion" : "ubicación " ,
            "Organizador" : "Id Organizador" ,

           
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(EventoForm,self).__init__(*args,**kwargs)
        
        self.fields['fecha']
        self.fields['nom'].empty_label="Selecciona"
       # self.fields['nom'].required=True
        self.fields['idOrganizador'].required=False
        