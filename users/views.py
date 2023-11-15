from django.shortcuts import render, reverse, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect

from .models import Nota, User

import datetime

# Create your views here.

#--------------PAGINAS PRINCIPALES----------------
def inicio(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")
    
class quizz(LoginRequiredMixin, generic.TemplateView):
    template_name = "quizz.html"

@csrf_protect
def send(request):
    if request.method == 'POST':
        if 'cantidad_correctas' in request.POST:
            cantidad_correctas = request.POST['cantidad_correctas']
            print(cantidad_correctas)
            tiempo = datetime.datetime.now()
            current_user = request.user
            print(current_user)
            print(tiempo)
            Nota.objects.create(
                usuario = current_user,
                nota = cantidad_correctas,
                fecha_evaluacion = tiempo
            )
            return HttpResponse('Correcto')
    return HttpResponse('Revisar')


#------------------Apartado administracion-----------------------
class listadoUsuarios(LoginRequiredMixin, ListView):
    template_name = "usuarios/listado.html"
    queryset = User.objects.all()
    context_object_name = "usuarios"

class detalleUsuario(LoginRequiredMixin, DetailView):
    template_name = "usuarios/detalle.html"
    queryset = User.objects.all()
    context_object_name = "usuario"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nota"] = Nota.objects.all()
        return context


#------------------Apartado usuario-----------------------
class perfilUsuario(LoginRequiredMixin, generic.TemplateView):
    template_name = "usuarios/perfil.html"
    queryset = User.objects.all()
    context_object_name = "usuario"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nota"] = Nota.objects.all()
        return context
    


#------------------MODULO 1-----------------------
def modulo1(request):
    return render(request, "modulo1/modulo1.html")

def fundamentos(request):
    return render(request, "modulo1/fundamentos.html")

def algoritmos(request):
    return render(request, "modulo1/algoritmos.html")

def comentarios(request):
    return render(request, "modulo1/comentarios.html")

def hola_mundo(request):
    return render(request, "modulo1/hola_mundo.html")

def ide_editor(request):
    return render(request, "modulo1/ide_editor.html")

def lenguajes(request):
    return render(request, "modulo1/lenguajes.html")

def programacion(request):
    return render(request, "modulo1/programacion.html")



#------------------MODULO 2-----------------------
def modulo2(request):
    return render(request, "modulo2/modulo2.html")

def concatenacion(request):
    return render(request, "modulo2/concatenacion.html")

def conversion(request):
    return render(request, "modulo2/conversion.html")

def entrada(request):
    return render(request, "modulo2/entrada.html")

def operadores(request):
    return render(request, "modulo2/operadores.html")

def variables(request):
    return render(request, "modulo2/variables.html")




#------------------MODULO 3-----------------------
def modulo3(request):
    return render(request, "modulo3/modulo3.html")

def anidados(request):
    return render(request, "modulo3/anidados.html")

def belif(request):
    return render(request, "modulo3/elif.html")

def bfor(request):
    return render(request, "modulo3/for.html")

def bif(request):
    return render(request, "modulo3/if.html")

def multiples(request):
    return render(request, "modulo3/multiples.html")

def bwhile(request):
    return render(request, "modulo3/while.html")


#------------------MODULO 4-----------------------
def modulo4(request):
    return render(request, "modulo4/modulo4.html")

def poo(request):
    return render(request, "modulo4/poo.html")

def clases(request):
    return render(request, "modulo4/clases.html")

def objetos(request):
    return render(request, "modulo4/objetos.html")

def constructor(request):
    return render(request, "modulo4/constructor.html")

def encapsulamiento(request):
    return render(request, "modulo4/encapsulamiento.html")

def herencia(request):
    return render(request, "modulo4/herencia.html")
