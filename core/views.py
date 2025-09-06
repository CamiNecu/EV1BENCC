from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"core/home.html")

def quienes(request):
    return render(request, "core/quienes.html")

def preguntasfre(request):
    return render(request, "core/preguntasfre.html")

def galimagenes(request):
    return render(request, "core/galimagenes.html")

# Create your views here.