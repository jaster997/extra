"""GameCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Inicio"),
    path('catalogo/', views.catalogo, name="Catalogo"),
    path('publico/', views.publico, name="Publico"),
    path('consulta/<int:id>/', views.consulta, name="Individual"),
    path('editarComentario/<int:id>/', views.editarConsulta, name="Editar"),
    path('eliminar/<int:id>/', views.eliminarConsulta, name="Borrar"),
    path('sugerencias/', views.sugerencias, name="Sugerencias"),
    path('mobiliarios/', views.mobiliario, name="Mobiliario"),
    path('accesorios/', views.accesorio, name="Accesorios"),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
