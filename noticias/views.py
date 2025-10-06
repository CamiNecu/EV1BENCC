## Vistas para la app 'noticias'.
##
## Esta vista obtiene todas las noticias, las pagina y pasa el objeto de
## la página actual a la plantilla para que muestre la lista paginada.

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Noticia


def Noticias(request):
        # Lista de noticias con paginación.
        # - Obtiene todas las instancias de Noticia desde la base de datos.
        # - Crea un `Paginator` para dividir la lista en páginas (aquí 1 por página).
        # - Lee el parámetro GET 'page' para saber qué página mostrar.
        # - `page_obj` contiene la página actual y utilidades (has_next, has_previous,
        #   paginator, número actual, etc.) que facilitan la paginación en la plantilla.
        # - Renderiza `noticias/noticias.html` pasando `page_obj` en el contexto.
        noticias_list = Noticia.objects.all()
        paginator = Paginator(noticias_list, 1)  # 1 noticia por página

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "noticias/noticias.html", {"page_obj": page_obj})