from socket import fromshare
from django import forms 
from .models import Servicio, Contratacion

class ServicioForm(forms.ModelForm):
  class Meta:
        model=Servicio
       #fields='__all__'
        fields=('idServicio','descripcion','costo')
        labels ={
            "idServicio" : "Código de Servicio" ,
            'descripcion': 'Descripción:',
            "costo" : "Costo" ,
                              
        }
        
    
  def __init__(self, *args, **kwargs):
        super(ServicioForm,self).__init__(*args,**kwargs)
        self.fields['idServicio'].empty_label="Selecciona"
        self.fields['descripcion'].required=True
        self.fields['costo'].required=False
        
        

class ContratacionForm(forms.ModelForm):
  class Meta:
        model=Contratacion
       #fields='__all__'
        fields=('idContratacion','fecha','idServicio','nomContratante')
        labels ={
            "idContratacion" : "Número de Contratacion" ,
            'fecha': 'Fecha contratación:',
            "idServicio" : "Cód de Servicio" ,
            'nomContratante':'Nombre del Contratante',
                              
        }
        
    
  def __init__(self, *args, **kwargs):
        super(ContratacionForm,self).__init__(*args,**kwargs)
     #   self.fields['nom'].empty_label="Selecciona"
        self.fields['idContratacion'].required=True
        self.fields['fecha'].required=True
        self.fields['nomContratante'].required=False        
        