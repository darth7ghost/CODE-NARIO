from django.urls import path
from .views import listadoUsuarios, detalleUsuario, perfilUsuario

from django.conf import settings
from django.conf.urls.static import static

app_name = "usuarios"

urlpatterns = [
    path('perfil/', perfilUsuario.as_view(), name='perfil'),
    path('listado/', listadoUsuarios.as_view(), name='listado'),
    path('listado/<int:pk>/', detalleUsuario.as_view(), name='detalle')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)