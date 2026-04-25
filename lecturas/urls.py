from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import FormularioView

urlpatterns = [
   
    path('', views.listar_lecturas, name="Lecturas"),
    #path('abonadoindex',views.FormularioView, name="FormularioAbonados"),
   #path('registrarAbonado/', FormularioView.index, name='registrarAbonado'),
   # path('guardarAbonado/', FormularioView.procesar_formulario, name='guardarAbonado'),
    path('formulario/', views.Formulario2, name='formulario2'),
    path('registrarAbonado/', views.FormularioView.index, name='registrarAbonado'),
    path('guardarAbonado/', views.FormularioView.procesar_formulario, name='guardarAbonado'),
    path('listar_pendientes/', views.listar_pendientes, name="listar_pendientes"),
    path('editarabonado/<int:id_abonado>',views.FormularioView.edit, name='editarabonado'),
    path('actualizar_abonado/<int:id_abonado>', views.FormularioView.actualizar_abonado, name='actualizar_abonado'),
    path('exportar_lecturas/', views.FormularioView.exportar_excel, name='exportar_excel'),

]