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






def busqueda(request):
       return render(request, 'appcoder/busqueda.html')

    

def buscar(request): 
     if request.GET["camada"]:
          camada = request.GET['camada']
          cursos = Curso.objects.filter(camada__icontains=camada)
          return render(request,"appcoder/resultadoBusqueda.html", {"cursos":cursos, "camada":camada})
     
     else:
          respuesta = "No enviaste datos"


          return HttpResponse(respuesta)
     


def resultadoBusqueda(request):

 return render(request, 'appcoder/resultadoBusqueda.html')







def agregarProfesores(request):
     
     if request.method =="POST":
          profesor = Profesor(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'],profesion=request.POST['email'])
          profesor.save()
          return render(request,"appcoder/index.html")
     
     return render(request, 'appcoder/agregarProfesores.html')




def leerProfesores(request):

      profesores = Profesor.objects.all() 

      contexto= {"profesores":profesores} 

      return render(request, "appCoder/leerProfesores.html",contexto)



def eliminarProfesor(request, profesor_nombre):
     profesor = Profesor.objects.get(nombre=profesor_nombre)
     profesor.delete()

     profesores = profesor = Profesor.objects.all()

     contexto= {"profesores":profesores}

     return render(request, "appCoder/leerProfesores.html")

def editarProfesor(request, profesor_nombre):
     profesor = Profesor.objects.get(nombre= profesor_nombre)

     if request.method == "POST":
          miFormulario = agregarProfesores(request.POST)
          print(miFormulario)

          if miFormulario.is_valid():
               informacion = miFormulario.cleaned_data

               profesor.nombre = informacion['nombre']
               profesor.apellido = informacion['apellido']
               profesor.email = informacion['email']
               profesor.profesion = informacion['profesion']

               profesor.save()

               return render(request, "appCoder/index.html")

     else:
          miFormulario = agregarProfesores(initial= {'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email':profesor.email, 'profesion': profesor.profesion})    
          return render(request,"appCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre} )


def profesores(request):
      return render(request,'appcoder/profesores.html')








def estudiantes(request):
     
     if request.method =="POST":
          estudiante = Estudiante(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'])
          estudiante.save()
          return render(request,"appcoder/index.html")
     
     return render(request, 'appcoder/estudiantes.html')

def leerEstudiantes(request):

      estudiantes = Estudiante.objects.all() 

      contexto= {"estudiantes":estudiantes} 

      return render(request, "appCoder/leerEstudiantes.html",contexto)



def eliminarEstudiante(request, estudiante_nombre):
     estudiantes = Estudiante.objects.get(nombre=estudiante_nombre)
     estudiantes.delete()

     estudiantes = estudiante = Estudiante.objects.all()

     contexto= {"estudiantes":estudiantes}

     return render(request, "appCoder/leerEstudiantes.html")