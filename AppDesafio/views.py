from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from AppDesafio.models import Productos
from AppDesafio.models import Categorias
from AppDesafio.models import Vendedores

from AppDesafio.forms import CategoriasFormulario
from AppDesafio.forms import ProductosFormulario
from AppDesafio.forms import VendedoresFormulario

def busqueda(request):
    busqueda = request.GET.get('producto')
    print(busqueda)
    productos_a = Productos.objects.filter(producto = busqueda)
    return render(request,'AppDesafio/resultadoproductos.html',{"busqueda": busqueda, "productos": productos_a})

# Create your views here.
def inicio(request):
    return render(request,'AppDesafio/inicio.html')    

def productos(request):
        if request.method == "POST":
            productosForms = ProductosFormulario(request.POST)
            print(productosForms)

            if productosForms.is_valid:
                informacion = productosForms.cleaned_data
                productos = Productos(producto=informacion["producto"], precio=informacion["precio"], stock=informacion["stock"])
                productos.save()
                return render(request, "AppDesafio/inicio.html")
        else:
            productosForms = ProductosFormulario()

        return render(request,'AppDesafio/productos.html', {'productosForms':productosForms})  


def categorias(request):
        if request.method == "POST":
            categoriasForms = CategoriasFormulario(request.POST)
            print(categoriasForms)

            if categoriasForms.is_valid:
                informacion = categoriasForms.cleaned_data
                categoria = Categorias(categoria=informacion["categoria"], subcategoria=informacion["subcategoria"])
                categoria.save()
                return render(request, "AppDesafio/inicio.html")
        else:
            categoriasForms = CategoriasFormulario()

        return render(request,'AppDesafio/categorias.html', {'categoriasForms':categoriasForms}) 
    
def vendedores(request):  
        if request.method == "POST":
            vendedoresForms = VendedoresFormulario(request.POST)
            print(vendedoresForms)

            if vendedoresForms.is_valid:
                informacion = vendedoresForms.cleaned_data
                vendedores = Vendedores(nombre=informacion["nombre"], cantidadProductos=informacion["cantidadProductos"], fecha_ingreso=informacion["fecha_ingreso"], mail=informacion["mail"])
                vendedores.save()
                return render(request, "AppDesafio/inicio.html")
        else:
            vendedoresForms = VendedoresFormulario()

        return render(request,'AppDesafio/vendedores.html', {'vendedoresForms':vendedoresForms})

def productosapi(request):
    losProductos = Productos.objects.all()
    return HttpResponse(serializers.serialize('json',losProductos))

def categoriasapi(request):
    lasCategorias = Categorias.objects.all()
    return HttpResponse(serializers.serialize('json',lasCategorias))

def vendedoresapi(request):
    losVendedores = Vendedores.objects.all()
    return HttpResponse(serializers.serialize('json',losVendedores))