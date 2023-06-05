"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token  # para crear tokens web JSON
# para obtener la identidad de un JWT en la ruta protegida
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required  # para proteger rutas
from flask_jwt_extended import JWTManager

api = Blueprint('api', __name__)


# REGISTRARSE
@api.route('/signup', methods=['POST'])
def register():
    data = request.json  # Obtenemos los datos enviados en la solicitud
    # Verificamos si el correo electrónico ya está registrado en la base de datos
    taken = User.query.filter_by(email=data.get('email')).first()
    print(data)
    print(taken)
    if not taken:  # si el email no esta registrado
        # creamos un nuevo usuario con email y password
        user = User(email=data.get('email'), password=data.get('password'))
        # agregamos al usuario a la sesion de base de datos
        db.session.add(user)
        db.session.commit()  # guardamos cambios

        # creamos un token de acceso, que se utiliza para autenticar al usuario
        token = create_access_token(identity=user.id)

        # devolcemos una respuesta json con el token y los detalles serializados
        return jsonify({'token': token, 'user': user.serialize()}), 200
    else:
        return jsonify({'error': 'correo ya existe'}), 404


@api.route('/login', methods=['POST'])
def login():
    data = request.json
    # creamos un nuevo usuario con email y password
    user = User.query.filter_by(email=data.get('email'), password=data.get('password')).first()

    if user is not None:
        token = create_access_token(identity=user.id)
        return jsonify({'token': token, 'user': user.serialize()}), 200
    else:
        return jsonify({'error': 'email y password no existen '})


@api.route('/private', methods=['GET'])
@jwt_required()  # Protege la ruta, requiere autenticación JWT
def get_private_acces():
    return 'esto es datos privados'


@api.route('/usersAll', methods=['GET'])
def user_all():
    users = User.query.all()
    data = [user.serialize() for user in users]
    return jsonify(data)


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3002))
    api.run(host='0.0.0.0', port=PORT, debug=True)


# """
# This module takes care of starting the API Server, Loading the DB and Adding the endpoints
# """
# import os
# from flask import Flask, request, jsonify, url_for, Blueprint
# from api.models import db, User
# from api.utils import generate_sitemap, APIException
# from flask_jwt_extended import create_access_token #para crear tokens web JSON
# from flask_jwt_extended import get_jwt_identity #para obtener la identidad de un JWT en la ruta protegida
# from flask_jwt_extended import jwt_required #para proteger rutas
# from flask_jwt_extended import JWTManager

# api = Blueprint('api', __name__)


# #REGISTRARSE
# @api.route('/signup', methods=['POST'])
# def register():
#     new_user={}
#     data = request.json #Obtenemos los datos enviados en la solicitud
#     new_user = User(email=('email'), password = ('password'))
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'msg':'usuario registrado'})


# if __name__ == '__main__':
#     PORT = int(os.environ.get('PORT', 3001))
#     api.run(host='0.0.0.0', port=PORT, debug=False)


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#      response_body = {
#          "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#      }

#      return jsonify(response_body), 200
