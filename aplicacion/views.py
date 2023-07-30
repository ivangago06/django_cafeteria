from django.shortcuts import render
from .models import project

def aplicacion(request):
    projects = project.objects.all()
    return render(request, "aplicacion/aplicacion.html",
                  {'projects':projects})  # <=====