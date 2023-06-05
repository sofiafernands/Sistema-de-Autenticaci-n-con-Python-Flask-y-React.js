"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os #modelulo para interactuar con el sistema operativo
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from api.utils import APIException, generate_sitemap
from api.models import db
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands
from flask_jwt_extended import JWTManager # importamos jwt
from flask_jwt_extended import create_access_token   #para crear tokens web JSON
from flask_jwt_extended import jwt_required  #para proteger rutas
from flask_jwt_extended import get_jwt_identity   #para obtener la identidad de un JWT en la ruta protegida


#from models import Person

ENV = os.getenv("FLASK_ENV")
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../public/')

app = Flask(__name__)
app.url_map.strict_slashes = False


# database condiguration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db, compare_type = True)
db.init_app(app)


# Allow CORS requests to this API / # Permitir solicitudes CORS a esta API
CORS(app)
setup_commands(app)
app.config["JWT_SECRET_KEY"] = os.getenv("FLASK_APP_KEY")  # Change this! / cambia esto
jwt = JWTManager(app)


# add the admin / # agregar el administrador
setup_admin(app)
setup_commands(app)

# Add all endpoints form the API with a "api" prefix / # Agregue todos los endpoints de la API con un prefijo "api"
app.register_blueprint(api, url_prefix='/api')

# Handle/serialize errors like a JSON object / # Manejar/serializar errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints / # generar un mapa del sitio con todos sus endpoints
@app.route('/')
def sitemap():
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')

# any other endpoint will try to serve it like a static file / # cualquier otro endpoint intentará servirlo como un archivo estático
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = 'index.html'
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0 # avoid cache memory
    return response


# this only runs if `$ python src/main.py` is executed / # esto solo se ejecuta si se ejecuta `$ python src/main.py`
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
    
