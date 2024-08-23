from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso,Estudiante,Profesor

def inicio(request):
    return render(request,'appcoder/index.html')



def entregables(request):
      return render(request,'appcoder/entregables.html')


def cursos(request):
     
     if request.method =="POST":
          curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
          curso.save()
          return render(request,"appcoder/index.html")
     
     return render(request, 'appcoder/cursos.html')

def estudiantes(request):
     
     if request.method =="POST":
          estudiante = Estudiante(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'])
          estudiante.save()
          return render(request,"appcoder/index.html")
     
     return render(request, 'appcoder/estudiantes.html')

def profesores(request):
     
     if request.method =="POST":
          profesor = Profesor(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'],profesion=request.POST['email'])
          profesor.save()
          return render(request,"appcoder/index.html")
     
     return render(request, 'appcoder/profesores.html')




def busquedaCamada(request):
     if request.GET["camada"]:
          camada= request.Get['camada']
          cursos = Curso.objects.filter(camada__icontains=camada)
          return render(request,"appcoder/busquedaCamada.html", {"cursos":cursos, "camada":camada})
     
     else:
          respuesta = "No enviaste datos"


     return HttpResponse(respuesta)
