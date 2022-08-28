from django.shortcuts import render, redirect
from .models import empresas, productos, comunidad
from .forms import comentarioForm, empresasForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'inicio/index.html')

def catalogo(request):

    return render(request, 'inicio/catalogo.html')

def mobiliario(request):
    catalogo= productos.objects.filter(categoria="Mobiliario")
    return render(request, 'inicio/productos.html', {'catalogo': catalogo})

def accesorio(request):
    catalogo= productos.objects.filter(categoria="Accesorio")
    return render(request, 'inicio/productos.html', {'catalogo': catalogo})

def publico(request):
    comuni= comunidad.objects.all()
    if request.method== 'POST':
        form= comentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Publico')
    form = comentarioForm()
    return render(request, 'inicio/publico.html', {'comuni': comuni})

def consulta(request, id):
    comuni= comunidad.objects.get(id=id)
    return render(request, 'inicio/editar.html', {'comuni': comuni})

def editarConsulta(request, id):
    comunida= get_object_or_404(comunidad, id=id)
    form= comentarioForm(request.POST, instance=comunida)
    if form.is_valid():
        form.save()
        comuni= comunidad.objects.all()
        return render(request, 'inicio/publico.html', {'comuni': comuni})

    return render( request, 'inicio/editar.html', {'comunida': comunida})


def eliminarConsulta(request, id, eliminar= 'inicio/eliminar.html'):
    comunida= get_object_or_404(comunidad, id=id)
    if request.method== 'POST':
        comunida.delete()
        comuni= comunidad.objects.all()
        return render(request, 'inicio/publico.html', {'comuni': comuni})

    return render(request, eliminar, {'object': comunida})



def sugerencias(request):
    if request.method == 'POST':
        form = empresasForm(request.POST, request.FILES)
        if form.is_valid():
            proveedor= request.POST['proveedor']
            sugerencia= request.POST['sugerencia']
            archivo= request.FILES['archivo']
            insert= empresas(proveedor=proveedor, sugerencia=sugerencia, archivo=archivo)
            insert.save()
            return render(request, 'inicio/sugerencias.html')
        else:
            messages.error(request, 'No se pudo subir el archvio de sugerencias')
    else:
        return render(request, 'inicio/sugerencias.html')