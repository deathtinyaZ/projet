from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from controlers.user_controler import UsersControler


#app = Flask(__name__)

#Engine = create_engine('mysql://root:root@192.168.99.100:3306/user')

#Session = sessionmaker(bind=engine)

#Base = declarative_base()

#Base.metadate.create_all(engine)

#session = Session ()

#mysql = MySQL(app)

#@app.route('/user',methods=['POST'])
#def create_user():
    #if not request.json or not 'name' in request.json or not 'surname' in request.json or not 'email' in request.json or not 'password' in request.json or not 'login' in request.json: 
        #abort(400)

#session.add(user)
#session.commit()
#session.close()

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root:@192.168.99.100:3306/user'

db = SQLAlchemy(app)

UsersControler.register(app)

if __name__ == "__main__":
    app.run(debug=True)
    