from django.urls import path
from AppDesafio import views

urlpatterns = [
    path("inicio", views.inicio,name='Inicio'),
    path("productos/", views.productos,name='Productos'),
    path("categorias/", views.categorias,name='Categorias'),
    path("vendedores/", views.vendedores,name='Vendedores'),
    path("Api/productos", views.productosapi),
    path("Api/categorias", views.categoriasapi),
    path("Api/vendedores", views.vendedoresapi),
    path("busqueda/", views.busqueda, name='productos'),
]
