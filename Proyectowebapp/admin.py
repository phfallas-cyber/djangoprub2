from django.contrib import admin
from import_export import resources
from lecturas.models import Caragral
from import_export.admin import ImportExportModelAdmin



class CaragralResource(resources.ModelResource):
    class Meta:
        model= Caragral

class CaragralAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CaragralResource

# Register your models here.

admin.site.register(Caragral, CaragralAdmin)
