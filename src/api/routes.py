"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User,Characters,Planets
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token  # para crear tokens web JSON
# para obtener la identidad de un JWT en la ruta protegida
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required  # para proteger rutas
from flask_jwt_extended import JWTManager

api = Blueprint('api', __name__)


#USER PLURALMENTE
@api.route('/user', methods=['GET'])
def handle_userAll():

    users = User.query.all() 
    data = [user.serialize() for user in users ] 
    return jsonify(data), 200 #aqui lo convertimos en string con jsonify

#USER SINGLE
@api.route('/user/<int:id>', methods=['GET'])
def get_userSingle(id):

    user = User.query.get(id) #se obtiene el usuario de la base de datos utilizando User.query.get(id)
    
    if user is None: #Si user es None, se lanza la excepción APIException con el mensaje "This user does not exist" y el codigo de estado 400.
        raise APIException('This user does not exist', status_code=400)
    
    return jsonify(user.serialize()), 200

#DELETE USER (ID)
@api.route('/user/<int:id>', methods=['DELETE'])
def delete_userSingle(id): #esta funcion recibe el parámetro id, que se obtiene de la URL.
        
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

# ALL THE CHARACTERS
@api.route('/characters', methods=['GET'])
def handle_charactersAll():

    charactersAll = Characters.query.all() #almacenamos todos los usuarios
    data = [character.serialize() for character in charactersAll] # para cada character dentro de los characters y nos lo serialice
    return jsonify(data), 200 #aqui lo convertimos en string con jsonify

#CHARACTERS SINGLE
@api.route('/characters/<int:id>', methods = ['GET'])
def get_characterSingle(id):
    characters = Characters.query.get(id)

    if characters is None: #Si characters es None(no existe el id ingresado), se lanza la excepción APIException con el mensaje "This user does not exist" y el codigo de estado 400.
        raise APIException('This Character does not exist', status_code=400)
    
    print(characters.serialize())
    return jsonify(characters.serialize()), 200

#CREATE NEW CHARACTER
@api.route('/characters', methods = ['POST']) #ruta para aceptar solicitudes y crear nuevo usuario
def create_newCharacter(): #def create_newCharacte(): Esta función se ejecutará cuando se acceda a la ruta /user mediante una solicitud POST.
 #se guarda el contenido en la variable "body"
    body = request.json

    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'name' not in body or not body['name']:
        raise APIException("You need to specify the name, can't be empty", status_code=400)
    if 'gender' not in body or not body['gender']:
        raise APIException("You need to specify the gender,can't be empty" , status_code=400)
    if 'eye_color' not in body or not body['eye_color']:
        raise APIException("You need to specify the eye_color, can't be empty" , status_code=400)

    print(body)
    characters = Characters(name = body["name"], gender=body["gender"], eye_color=body["eye_color"]) #se crea un objeto de la clase User con los valores del correo electrónico y el estado activo obtenidos del objeto body.
    db.session.add(characters) #esto indica que se debe crear un nuevo registro en la base de datos con los valores proporcionados.
    db.session.commit() #Realiza una confirmación en la sesión de la base de datos, lo que efectivamente guarda los cambios realizados en la base de datos.

    response_body = {
         "msg": "a new character has been added",
     } # Creamos un diccionario llamado response_body que contiene un mensaje indicando que el usuario ha sido creado.

    return jsonify(response_body), 200 #La función jsonify se utiliza para convertir el diccionario en una respuesta JSON valida

#DELETE CHARACTER(ID)
@api.route('/characters/<int:id>', methods=['DELETE'])
def delete_charactersSingle(id): #esta funcion recibe el parámetro id, que se obtiene de la URL.

    characters = Characters.query.get(id)
    if characters:
        db.session.delete(characters)
        db.session.commit()
        return jsonify({'message': 'character deleted successfully'}), 200
    else:
        return jsonify({'message': 'Character not found'}), 404

# ALL THE PLANETS
@api.route('/planets', methods=["GET"])
def handle_planetsAll():
    planetsAll= Planets.query.all()
    data = [planet.serialize() for planet in planetsAll] # para cada planet dentro de los planetaS y nos lo serialice

    return jsonify(data), 200

#PLANET SINGLE(ID)
@api.route('/planets/<int:id>', methods=["GET"])
def get_planetSingle(id):

    planet = Planets.query.get(id)

    if planet is None: #Si el planet es None(no existe el id ingresado), se lanza la excepción APIException con el mensaje "This user does not exist" y el codigo de estado 400.
        raise APIException('This Planet does not exist', status_code=400)
    
    print(planet.serialize())
    return (jsonify.serialize()), 200

#CREATE NEW PLANET
@api.route('/planets', methods=["POST"])
def create_newPlanet():

    body = request.json

    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'name' not in body or not body['name'].strip():
        raise APIException("You need to specify the name, can't be empty", status_code=400)
    if 'terrain' not in body or not body['terrain']:
        raise APIException("You need to specify the terrain can't be empty", status_code=400)
    if 'population' not in body or not body['population']:
        raise APIException("You need to specify the population, can't be empty", status_code=400)
    
    print(body)
    planets = Planets(name=body["name"], terrain=body["terrain"], population=body["population"])
    db.session.add(planets) #esto indica que se debe crear un nuevo registro en la base de datos con los valores proporcionados.
    db.session.commit()

    response_body = {
         "msg": "a new planet has been added",
     } # Creamos un diccionario llamado response_body que contiene un mensaje indicando que el nuevo planeta ha sido creado.

    return jsonify(response_body), 200

#DELETE PLANET (ID)
@api.route('/planets/<int:id>', methods = ["DELETE"])
def delete_planet(id):
    planet = Planets.query.get(id)
    if planet:
        db.session.delete(planet) #Esta línea elimina el objeto planet de la sesión de la base de datos.
        db.session.commit() # se guarda los cambios realizados en la base de datos. La eliminación del planeta se confirma al llamar a este método.
        return jsonify({'message': 'planet deleted succesfully'})
    else:
        return jsonify({'message':'Planet not found'}), 400

# REGISTRARSE
@api.route('/signup', methods=['POST'])
def register():
    print('hola')
    data = request.json  # Obtenemos los datos enviados en la solicitud
    if data is None:
        raise APIException("You need to specify the request data as a json object", status_code=400)
    if 'name' not in data or not data ['name']:  #se verifica que esta agregada la propiedad name y que no se ingrese el campo vacio
        raise APIException("You need to specify the name, can't be empty" , status_code=400)
    if 'email' not in data or not data['email']:
        raise APIException("You need to specify the email, can't be empty", status_code=400)

    # Verificamos si el correo electrónico ya está registrado en la base de datos
    taken = User.query.filter_by(email=data.get('email')).first()
    print(data)
    print(taken)
    if not taken:  # si el email no esta registrado
        # creamos un nuevo usuario con email y password
        user = User(email=data.get('email'), password=data.get('password'),name=data.get('name'))
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
    return 'esto es datos privados', 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3002))
    api.run(host='0.0.0.0', port=PORT, debug=True)


