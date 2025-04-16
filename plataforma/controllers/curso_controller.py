from plataforma.models.curso import Curso

def obtener_cursos():
    return Curso.objects.all()

def crear_curso(nombre, descripcion):
    curso = Curso(nombre=nombre, descripcion=descripcion)
    curso.save()
    return curso
