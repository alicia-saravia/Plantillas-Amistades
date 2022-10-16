from Amistades_app import app
from Amistades_app.controlador.controlador_usuario import Usuario
from Amistades_app.controlador.controlador_crear_amistad import Amistades_usuario


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración