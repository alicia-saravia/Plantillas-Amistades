from Amistades_app import app
from flask import render_template, request, redirect
from Amistades_app.modelo.modelo_usuario_amistad import Amistades_usuario

@app.route('/crear_amistad', methods=["POST"])
def creando_amigo():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "usuario_id": request.form["usuario_id"],
        "amigo_id" : request.form["amigo_id"],
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Amistades_usuario.haciendo_amigos(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404