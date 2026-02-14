from django.shortcuts import render

def index(request):
    context = {"mensaje" : "Bienvenido a mi aplicacion echa en Django"}
    return render(request, "myapp/index.html", context)
    