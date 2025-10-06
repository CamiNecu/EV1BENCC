from django.db import models


class Noticia(models.Model):
    # Modelo que representa una noticia o entrada.
    #
    # Campos:
    # - titulo: cadena corta para el título (máx 100 caracteres).
    # - detalle: texto largo con el contenido de la noticia.
    # - imagen: campo de imagen; los ficheros se guardan en la carpeta 'projects'.
    # - created: fecha/hora de creación (rellenada automáticamente).
    # - updated: fecha/hora de última modificación (se actualiza automáticamente).

    titulo = models.CharField(max_length=100)
    detalle = models.TextField()
    imagen = models.ImageField(
        upload_to="projects",
        verbose_name="Imagen"
    )

    # timestamps útiles para mostrar cuándo se publicó/actualizó la noticia
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        # Representación legible del objeto (útil en admin y debugging).
        return self.titulo
