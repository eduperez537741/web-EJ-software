from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import logging
import sys

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Obtener la ruta absoluta del directorio actual
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Asegurarse de que los directorios existan
for directory in [TEMPLATE_DIR, STATIC_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Directorio creado: {directory}")

app = Flask(__name__, 
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR)

@app.route('/')
def home():
    logger.debug("Accediendo a la página principal")
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    logger.debug("Accediendo a la página de servicios")
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    logger.debug("Accediendo a la página de contacto")
    return render_template('contacto.html')

@app.route('/nosotros')
def nosotros():
    logger.debug("Accediendo a la página nosotros")
    return render_template('nosotros.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    try:
        # Configuración del servidor
        print("\n" + "="*60)
        print(" "*20 + "EJ Software Solutions")
        print("="*60)
        print("\nIniciando servidor en puerto 5000...")
        print("\nPara acceder a la web:")
        print("1. Abre tu navegador web")
        print("2. Visita: http://localhost:5000")
        print("   o http://127.0.0.1:5000")
        print("\n" + "="*60 + "\n")

        # Iniciar el servidor
        app.run(
            debug=True,
            host='127.0.0.1',  # Solo escuchar en localhost
            port=5000,
            threaded=True
        )
    except Exception as e:
        logger.error(f"Error al iniciar el servidor: {str(e)}")
        print(f"\nError al iniciar el servidor: {str(e)}")
        print("\nPosibles soluciones:")
        print("1. Verifica que el puerto 5000 no esté en uso")
        print("2. Asegúrate de que no haya un firewall bloqueando el acceso")
        print("3. Intenta reiniciar la aplicación")
        print("\nSi el problema persiste, contacta al soporte técnico.")