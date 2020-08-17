from flask_sqlalchemy import SQLAlchemy
from models.user import User

db = SQLAlchemy()


def get_Users(): 
    Users = User.query.all()
    return Users

def get_user_by_id(user_id):
    return user_id

def create_user(user):
    db.session.add(user)
    db.session.commit()
    return user.id

def update_user(user_id): 
    return user_id

def delete_user(user_id):
    return user_id



