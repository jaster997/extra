from django.contrib import admin
from .models import empresas, productos, comunidad

# Register your models here.

class catalogo(admin.ModelAdmin):
    search_fields= ('nombre', 'categoria')
    list_display= ('id', 'nombre', 'categoria', 'precio', 'existencia')
    date_hierarchy= 'creacion'

admin.site.register(productos, catalogo)


class mensajes(admin.ModelAdmin):
    search_fields= ('nombre', 'producto')
    list_display= ('id', 'nombre', 'producto', 'mensaje')
    date_hierarchy= 'creacion'

admin.site.register(comunidad, mensajes)


class proveedor(admin.ModelAdmin):
    search_fields= ('proveedor', 'sugerencia')
    list_display= ('id', 'proveedor', 'sugerencia', 'archivo')
    date_hierarchy= 'creacion'

admin.site.register(empresas, proveedor)