from flask_sqlalchemy import SQLAlchemy

sqla = SQLAlchemy()

class User(sqla.Model):
    __tablename__= 'user'

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String)
    surname = sqla.Column(sqla.String)
    BD = sqla.Column(sqla.String)
    email = sqla.Column(sqla.String)
    password = sqla.Column(sqla.String)
    login = sqla.Column(sqla.String)

    def __init__(self, name, surname, tel, email, password, login):
        super().__init__()
        self.name = name
        self.surname = surname
        self.BD = BD
        self.email = email
        self.password = password
        self.login = login

    def __repr__(self):
        return f'<user id:{self.id} name:{self.name} surname:{self.surname} BD:{self.BD} email:{self.email} password:{self.password} login:{self.login}>'