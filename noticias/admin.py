from django.contrib import admin
from .models import Noticia


class ProjectAdmin(admin.ModelAdmin):
    # Configuración del admin para el modelo Noticia.
    #
    # - readonly_fields: campos que son visibles en el admin pero no editables
    #   (útil para timestamps auto-generados como created/updated).
    readonly_fields = ('created', 'updated')


# Registro del modelo con la clase de configuración. Esto hace que las
# noticias puedan gestionarse desde /admin/ en la interfaz de Django.
admin.site.register(Noticia, ProjectAdmin)
