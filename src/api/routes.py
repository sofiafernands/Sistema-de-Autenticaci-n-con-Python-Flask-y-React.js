"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token   #para crear tokens web JSON
from flask_jwt_extended import jwt_required  #para proteger rutas
from flask_jwt_extended import get_jwt_identity   #para obtener la identidad de un JWT en la ruta protegida


api = Blueprint('api', __name__)

#REGISTRARSE
@api.route('/signup', methods = ['POST'] )
def register_user():
    data = request.json #Obtenemos los datos enviados en la solicitud
    taken = User.query.filter_by(email=data.get('email')) #Verificamos si el correo electrónico ya está registrado en la base de datos
    if not taken: #si el email no esta registrado
        user = User (email=data.get('email'), password=data.get('password')) #creamos un nuevo usuario con email y password
        db.session.add(user) #agregamos al usuario a la sesion de base de datos
        db.session.commit() #guardamos cambios

        token = create_access_token(identity=user.id)#creamos un token de acceso, que se utiliza para autenticar al usuario

        return jsonify({'token':token,'user': user.serialize()}), 200 #devolcemos una respuesta json con el token y los detalles serializados
    else:
        return jsonify ({'error':'correo ya existe'}), 404 
    
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    api.run(host='0.0.0.0', port=PORT, debug=False)


    


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }

#     return jsonify(response_body), 200