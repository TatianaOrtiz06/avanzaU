from plataforma.models.usuario import Usuario

class UsuarioRepository:
    def obtener_por_usuario(self, username):
        return Usuario.objects.filter(usuario=username).first()
