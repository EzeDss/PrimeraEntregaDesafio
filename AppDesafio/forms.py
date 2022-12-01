from django import forms

class ProductosFormulario(forms.Form):
    producto=forms.CharField(max_length=40)
    precio=forms.IntegerField()
    stock=forms.IntegerField()

class CategoriasFormulario(forms.Form):
    categoria=forms.CharField(max_length=40)
    subcategoria=forms.CharField(max_length=40)

class VendedoresFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    cantidadProductos=forms.IntegerField()
    fecha_ingreso=forms.DateField()
    mail = forms.EmailField(max_length=200)

#    , blank=True, null=True