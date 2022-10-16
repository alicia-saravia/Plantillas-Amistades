from Amistades_app.configuracion.mysqlconnection import connectToMySQL

class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    @classmethod
    def todos_usuarios(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        resultado = connectToMySQL('Amistades').query_db(query)
        amigos = []
        for amigo in resultado:
            amigos.append(cls(amigo))
        return amigos 
        
    @classmethod
    def crear_usuario(cls, data ):
        query = "INSERT INTO usuarios ( nombre, apellido) VALUES ( %(nombre)s , %(apellido)s);"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('Amistades').query_db( query, data )
