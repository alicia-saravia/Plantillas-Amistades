from Amistades_app import app
from flask import render_template, request, redirect
from Amistades_app.modelo.modelo_usuario import Usuario
from Amistades_app.modelo.modelo_usuario_amistad import Amistades_usuario


@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def todos_usuario():
    usuario = Usuario.todos_usuarios()
    amistades = Amistades_usuario.amistad_usuario()
    print(amistades)
    print(usuario)
    return render_template("index.html", usuarios = usuario, amistades = amistades)

@app.route('/crear_amigo', methods=["POST"])
def creando_usuarios():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Usuario.crear_usuario(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404