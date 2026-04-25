from django.contrib import admin
from .models import Categoria,Post
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


#ahora voy a registrar las tablas para que sean vistas en el admin de django
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)
