from django.shortcuts import render
from .models import Noticia
def Noticias(request):
    noticia=Noticia.objects.all()
    return render(request,"noticias/noticias.html",
                  {"noticia":noticia})