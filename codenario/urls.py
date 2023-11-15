"""
URL configuration for codenario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from users.views import (inicio, modulo1, modulo2, modulo3, modulo4, about, quizz, send,
                        algoritmos, comentarios, fundamentos, hola_mundo, ide_editor, lenguajes, programacion,
                        concatenacion, conversion, entrada, operadores, variables,
                        anidados, belif, bfor, bif, multiples, bwhile,
                        poo, clases, objetos, constructor, encapsulamiento, herencia,
                        SignupView) 

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('index/', inicio, name="inicio"),
    path('inicio/', inicio, name="inicio"),
    path('about/', about, name="about"),
    path('acercade/', about, name="about"),
    path('quizz/', quizz.as_view(), name="quizz"),
    path('send/', send, name="send"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    #-----MODULO 1-------
    path('modulo1/', modulo1, name="modulo1"),
    path('modulo1/algoritmos', algoritmos, name="algoritmos"),
    path('modulo1/comentarios', comentarios, name="comentarios"),
    path('modulo1/fundamentos', fundamentos, name="fundamentos"),
    path('modulo1/hola_mundo', hola_mundo, name="hola_mundo"),
    path('modulo1/ide_editor', ide_editor, name="ide_editor"),
    path('modulo1/lenguajes', lenguajes, name="lenguajes"),
    path('modulo1/programacion', programacion, name="programacion"),
    #-----MODULO 2--------
    path('modulo2/', modulo2, name="modulo2"),
    path('modulo2/concatenacion', concatenacion, name="concatenacion"),
    path('modulo2/conversion', conversion, name="conversion"),
    path('modulo2/entrada', entrada, name="entrada"),
    path('modulo2/operadores', operadores, name="operadores"),
    path('modulo2/variables', variables, name="variables"),
    #-----MODULO 2--------
    path('modulo3/', modulo3, name="modulo3"),
    path('modulo3/anidados', anidados, name="anidados"),
    path('modulo3/elif', belif, name="elif"),
    path('modulo3/for', bfor, name="for"),
    path('modulo3/if', bif, name="if"),
    path('modulo3/multiples', multiples, name="multiples"),
    path('modulo3/while', bwhile, name="while"),
    #-----MODULO 2--------
    path('modulo4/', modulo4, name="modulo4"),
    path('modulo4/poo', poo, name="poo"),
    path('modulo4/clases', clases, name="clases"),
    path('modulo4/objetos', objetos, name="objetos"),
    path('modulo4/constructor', constructor, name="constructor"),
    path('modulo4/encapsulamiento', encapsulamiento, name="encapsulamiento"),
    path('modulo4/herencia', herencia, name="herencia"),
    #-----USUARIOS--------
    path('usuarios/', include('users.urls', namespace="usuarios")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
path('usuario/', include('users.urls'), namespace="usuarios")
"""
