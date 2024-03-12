from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#----------------------------------------------------------------
class LoginForm(AuthenticationForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=30, required=True, help_text='Requerido. Ingrese su nombre.')
    apellido = forms.CharField(max_length=30, required=True, help_text='Requerido. Ingrese su apellido.')
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo válida.')
    usuario = forms.CharField(max_length=50, required=True, help_text= "Ingrese su nombre de usuario visible")
    password = forms.CharField(max_length=50, required=True, help_text= "Ingrese su password secreta")

class AgregarProd(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = forms.IntegerField(required=True)
    tipo = forms.CharField(max_length=50, required=True, help_text='Tipos hasta ahora: "grafica","procesador","monitor" ')

class ComprarProd(forms.Form):
    nombre_prod = forms.CharField(max_length=100)
    precio = forms.IntegerField(required=True)
    cantidad = forms.IntegerField(required=True)
    

