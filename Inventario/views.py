from django.shortcuts import render
from .models import *
from .templates import *
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "inventario/home.html")

def tienda(request):
    context = {'productos': Producto.objects.all()}
    return render(request, "inventario/tienda.html", context)

def tickets(request):
    context = {'facturas': Factura.objects.all()}
    return render(request, 'inventario/facturas.html', context)

def graficas(request):
    context = {'productos': Producto.objects.filter(tipo = 'grafica')}
    return render(request, "inventario/graficas.html", context)

def procesadores(request):
    context = {'productos': Producto.objects.filter(tipo = 'procesador')}
    return render(request, "inventario/procesadores.html", context)

def monitores(request):
    context = {'productos': Producto.objects.filter(tipo = 'monitor')}
    return render(request, "inventario/monitores.html", context)

def usuarios_registrados(request):
    context = {'usuarios': Usuario.objects.all()}
    return render(request, "inventario/usuarios.html", context)

def comprar(request):
    context = {'productos': Producto.objects.all()}
    return render(request, "inventario/menucompra.html", context)


#--------------- Formularios ---------------#
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import *

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():

            user_username = form.cleaned_data.get('usuario')
            user_password = form.cleaned_data.get('password')
            user_email = form.cleaned_data.get('email')
            user_first_name = form.cleaned_data.get('nombre')
            user_last_name = form.cleaned_data.get('apellido')

            user = Usuario(nombre = user_first_name,
                           apellido = user_last_name,
                           email = user_email,
                           usuario = user_username,
                           password = user_password)
            user.save()
            return render(request, "inventario/home.html")  
        else:
            form = RegistroForm()
    return render(request, 'inventario/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            # Autenticar al usuario
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return render(request, 'inventario/tienda.html')  # Reemplaza 'home' con la URL a la que quieres redirigir después del inicio de sesión
    else:
        form = LoginForm()

    return render(request, 'inventario/iniciar_sesion.html', {'form': form})

def agregar_prod(request):
    if request.method == "POST":
        form = AgregarProd(request.POST)
        if form.is_valid():
            pnombre = form.cleaned_data.get('nombre')
            pprecio = form.cleaned_data.get('precio')
            pstock = form.cleaned_data.get('stock')
            ptipo = form.cleaned_data.get('tipo')
            
            producto = Producto(nombre = pnombre, precio = pprecio, stock = pstock, tipo = ptipo)
            
            producto.save()
            return render(request, "inventario/home.html") 
    else:
        form = AgregarProd()
    return render(request, 'inventario/addprod.html', {'form': form})

def comprar_prod(request):
    if request.method =="POST":
        form = ComprarProd(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            precio = form.cleaned_data.get('precio')
            cant = form.cleaned_data.get('cantidad')

            carro = Factura(nombre_prod = nombre, total = precio*cant, fecha = datetime.now() )
            carro.save()
    else:
        form = ComprarProd()

    return render(request, 'inventario/tienda.html', {'form': form})

#---------------------Busquedas

def buscarProducto(request):
    return render(request, "inventario/buscarProd.html")    

def encontrarProducto(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {'productos': productos}
    else:
        contexto = {'productos': Producto.objects.all()}

    
    return render(request, 'inventario/encontrarProd.html', contexto)   

