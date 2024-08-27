from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('deportes/nosotros',views.nosotros,name='nosotros'),
    path('deportes/listaD',views.listaD,name='listaD'),
    path('deportes/<int:id>/',views.crear_editaDeporte,name='crear_editarDeporte'),
    path('deportes/eliminar/<int:id>',views.eliminar,name='eliminar'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)