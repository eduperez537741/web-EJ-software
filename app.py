from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import logging
import socket
import time
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

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('0.0.0.0', port))
            return False
        except socket.error:
            return True

def find_available_port(start_port=8081, max_attempts=10):
    for port in range(start_port, start_port + max_attempts):
        if not is_port_in_use(port):
            return port
    return None

if __name__ == '__main__':
    # Intentar varios puertos si el 8081 está ocupado
    port = find_available_port()
    if port is None:
        print("\nError: No se pudo encontrar un puerto disponible.")
        print("Por favor, cierra otras aplicaciones o reinicia tu computadora.")
        print("Puertos intentados: 8081-8090")
        exit(1)

    # Verificar y crear directorios necesarios
    for directory in [TEMPLATE_DIR, STATIC_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Directorio creado: {directory}")

    # Mostrar información de inicio
    print("\n" + "="*60)
    print(" "*20 + "EJ Software Solutions")
    print("="*60)
    print(f"\nIniciando servidor en puerto {port}...")
    print("\nPara acceder a la web:")
    print("1. Abre tu navegador web")
    print(f"2. Visita: http://localhost:{port}")
    print(f"   o http://127.0.0.1:{port}")
    print("\nPáginas disponibles:")
    print(f"- Principal: http://localhost:{port}")
    print(f"- Servicios: http://localhost:{port}/servicios")
    print(f"- Nosotros: http://localhost:{port}/nosotros")
    print(f"- Contacto: http://localhost:{port}/contacto")
    print("\n" + "="*60 + "\n")

    # Registrar información en el archivo de log
    logger.info(f"Iniciando servidor en puerto {port}")
    logger.info(f"Directorio de templates: {TEMPLATE_DIR}")
    logger.info(f"Directorio estático: {STATIC_DIR}")

    try:
        # Configuración más permisiva para el servidor
        app.run(
            debug=True,
            host='0.0.0.0',
            port=port,
            use_reloader=False,
            threaded=True
        )
    except Exception as e:
        logger.error(f"Error al iniciar el servidor: {str(e)}")
        print(f"\nError: {str(e)}")
        print("Por favor, intenta reiniciar la aplicación o contacta al soporte.")