from flask_classful import FlaskView, route
from flask import jsonify
from flask import abort
from flask import request
import services.user_services as userService
from dto.user_dto import UserDto



class UsersControler(FlaskView):
    route_base = '/api/Users/'

    @route('/')
    def get_users(self):
        Users = userservices.get_Users()
        return jsonify(Users)

    @route('/<int:user_id>')
    def get_user_by_id(self,user_id):
        user = userservices.get_user_by_id(user_id)
        return jsonify(user)

    @route('/', methods=['POST'])
    def create_user(self):
        name = request.json['name'],
        surname = request.json['surname'],
        email = request.json['email'],
        login = request.json['login'],
        password = request.json['password']
        user = userDto(name, surname, email, login, password)
        return userservices.create_user(user)

    @route('/<int:user_id>', methods=['PUT'])
    def update_user(self, user_id):
        user = userservices.update_user(user_id)
        return jsonify(user)

    @route('/<int:user_id>', methods=['DELETE'])
    def delete_user(self, user_id):
        result = userservices.delete_user(user_id)
        return jsonify(result)



