from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

#se pone . para indicar que es de la misma ubicacion donde esta
#la aplicacion que se busca la carpeta views


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',views.home, name="Home"),
    #path('servicios', views.servicios, name="Servicios"),
    #path('tienda', views.tienda, name="Tienda"),
    #path('blog', views.blog, name="Blog"),
    path('',views.contacto, name="Contacto"),
    #path('lecturas', views.lecturas, name="Lecturas"),

]

