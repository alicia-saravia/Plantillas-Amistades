from Amistades_app.configuracion.mysqlconnection import connectToMySQL

class Amistades_usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.usuario_id = data['nombre']
        self.amigo_id = data['apellido']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    @classmethod
    def amistad_usuario(cls):
        query = """SELECT * FROM usuarios join usuarios_amistades on usuarios.id = usuarios_amistades.usuario_id
                    join usuarios as amigos on amigos.id = usuarios_amistades.amigo_id; """
        resultado = connectToMySQL('Amistades'). query_db(query)
        print(resultado)
        return resultado

    @classmethod
    def haciendo_amigos(cls, data):
        query = "INSERT  INTO usuarios_amistades (usuario_id, amigo_id) VALUES (%(usuario_id)s, %(amigo_id)s)"
        resultado = connectToMySQL('Amistades').query_db(query, data)
        return resultado