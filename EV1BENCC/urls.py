## URL configuration for EV1BENCC project.
##
## The `urlpatterns` list routes URLs to views. For more information please see:
##     https://docs.djangoproject.com/en/5.2/topics/http/urls/
## Examples:
## Function views
##     1. Add an import:  from my_app import views
##     2. Add a URL to urlpatterns:  path('', views.home, name='home')
## Class-based views
##     1. Add an import:  from other_app.views import Home
##     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
## Including another URLconf
##     1. Import the include() function: from django.urls import include, path
##     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
##
## Configuración de rutas (URLconf) del proyecto.
##
## Aquí se asocian rutas (paths) con vistas importadas desde las apps `core`
## y `noticias`. También se incluye el admin y la configuración para servir
## archivos media en modo DEBUG.

from django.contrib import admin
from django.urls import path
from core import views as views_core
from noticias import views as views_noticias
from django.conf import settings


urlpatterns = [
    # Ruta raíz -> vista 'home' de la app core
    path('', views_core.home, name='Home'),
    # Páginas informativas
    path('quienes/', views_core.quienes, name='Quienes somos'),
    path('preguntasfrecuentes/', views_core.preguntasfre, name='Preguntas frecuentes'),
    path('galeriaimagenes/', views_core.galimagenes, name='Galeria de imagenes'),
    # Sección de noticias
    path('noticias/', views_noticias.Noticias, name="noticias"),
    # Panel de administración de Django
    path('admin/', admin.site.urls),
]

# Durante el desarrollo (DEBUG=True) Django puede servir archivos media
# (como imágenes subidas) directamente usando `static()`; en producción
# normalmente se usan servidores web o servicios (S3, CDN, etc.).
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
