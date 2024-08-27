from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('deporte/nosotros',views.nosotros,name='nosotros'),
    path('deporte/listaD/',views.listaD,name='listaD'),
      path('deporte/crear_editarDeporteD/<int:idDeporte>/', views.crear_editarDeporteD, name='crear_editarDeporteD'),
    path('deporte/eliminar/<int:idDeporte>',views.eliminar,name='eliminar'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)