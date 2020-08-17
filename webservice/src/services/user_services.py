import repositories.userRepo as userRepo
from models.user import User
import jsonpickle


def get_users():
    users = userRepo.get_Users()
    return jsonpickle.encode(Users)

def get_user_by_id(user_id):
    return user_id

def create_user(userDto): 
    user =  User(userDto.name,userDto.surname,userDto.BD,userDto.email,userDto.password,userDto.login)
    data = userRepo.create_user(user)
    userDto = jsonpickle.encode(data,max_depth=2)
    return userDto

def update_user(user_id): 
    return user_id

def delete_user(user_id):
    return user_id