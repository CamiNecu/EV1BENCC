## Vistas de la aplicación `core`.
##
## Cada función recibe un objeto `request` y devuelve una respuesta HTTP.
## Usamos `render()` para combinar una plantilla con un contexto (datos) y
## devolver una página HTML.

from django.shortcuts import render, HttpResponse


def home(request):
        # Página principal.
        # - Construye una lista de obras (simulada aquí como datos estáticos)
        # - Pasa esa lista a la plantilla `core/home.html` mediante el contexto
        #   con la clave 'obras'
        # - Esto permite que la plantilla muestre las obras de manera dinámica
    obras = [
        {
            'titulo': 'La joven de la perla',
            'autor': 'Johannes Vermeer',
            'imagen': 'core/assets/img/JovenPerla.jpeg'
        },
        {
            'titulo': 'Autorretrato de Vincent Van Gogh (1889)',
            'autor': 'Vincent van Gogh',
            'imagen': 'core/assets/img/VincentSelf1889.jpg'
        },
        {
            'titulo': 'Der Kuss',
            'autor': 'Gustav Klimt',
            'imagen': 'core/assets/img/TheKiss.jpg'
        },
    ]
    return render(request, "core/home.html", {'obras': obras})


def quienes(request):
    # Renderiza la página 'Quiénes somos'.
    # No necesita contexto dinámico por ahora; solo devuelve la plantilla.
    return render(request, "core/quienes.html")


def preguntasfre(request):
    # Renderiza la página de preguntas frecuentes (FAQ).
    return render(request, "core/preguntasfre.html")


def galimagenes(request):
    # Renderiza la galería de imágenes.
    return render(request, "core/galimagenes.html")


# Nota: Estas vistas son funciones simples (function-based views). Para
# proyectos más grandes se pueden usar vistas basadas en clases (Class-Based Views)