from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profesor, Curso, Estudiante




# VISTAS BASADAS EN CLASES - Profesores
class ProfesoresListView(ListView):
    model = Profesor
    context_object_name = "profesores"
    template_name = "appCoder/Vistas_Clases/profesor_list.html"

    
class ProfesoresDetailView(DetailView):
    model = Profesor
    template_name = "leerProfesores.html"    


class ProfesoresCreateView(CreateView):
    
    model = Profesor
    template_name = "appcoder/Vistas_Clases/agregarProfesores.html"
    success_url = reverse_lazy('List')
    fields = ['nombre', 'apellido', 'email', 'profesion']
    

class ProfesoresUpdateView(UpdateView):
    model = Profesor
    success_url = reverse_lazy("List")
    template_name = "appcoder/Vistas_Clases/profesor_update.html"
    fields = ["nombre", "apellido", "email", "profesion"]    


class ProfesoresDeleteView(DeleteView):
    model = Profesor
    context_object_name = "profesores"
    template_name = "appcoder/Vistas_Clases/profesor_confirm_delete.html"
    success_url = reverse_lazy('List')
    



# VISTAS BASADAS EN CLASES - Cursos
class CursoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appCoder/Vistas_Clases/curso_list.html"

    
class CursoDetailView(DetailView):
    model = Curso
    template_name = "leerProfesores.html"    


class CursoCreateView(CreateView):
    
    model = Curso
    template_name = "appcoder/Vistas_Clases/agregar_cursos.html"
    success_url = reverse_lazy('CursoList')
    fields = ['nombre', 'camada']

    
    

class CursoUpdateView(UpdateView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    template_name = "appcoder/Vistas_Clases/curso_update.html"
    fields = ['nombre', 'camada'] 


class CursoDeleteView(DeleteView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appcoder/Vistas_Clases/curso_confirm_delete.html"
    success_url = reverse_lazy('CursoList')
    


# VISTAS BASADAS EN CLASES - Estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    context_object_name = "estudiantes"
    template_name = "appCoder/Vistas_Clases/estudiantes_list.html"

    
class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "leerProfesores.html"    


class EstudianteCreateView(CreateView):
    
    model = Estudiante
    template_name = "appcoder/Vistas_Clases/agregar_estudiantes.html"
    success_url = reverse_lazy('EstudianteList')
    fields = ["nombre", "apellido", "email"]
    

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    template_name = "appcoder/Vistas_Clases/estudiantes_update.html"
    fields = ["nombre", "apellido", "email"] 


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    context_object_name = "estudiantes"
    template_name = "appcoder/Vistas_Clases/estudiantes_confirm_delete.html"
    success_url = reverse_lazy('EstudianteList')
    

