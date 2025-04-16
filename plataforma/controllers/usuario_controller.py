from plataforma.models.usuario import Usuario

def obtener_usuarios():
    return Usuario.objects.all()

def obtener_usuario_por_id(usuario_id):
    return Usuario.objects.get(id=usuario_id)
