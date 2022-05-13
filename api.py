
import os
import sys

import flask 

import mysql.connector

import blueprints.test

from random import choice

app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(blueprints.test.blueprint)

conn = mysql.connector.connect(
    host=os.environ['DB_SERVER'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_DATABASE']
)

conn.autocommit=True
cursor = conn.cursor()


@app.route('/', methods=[ 'GET' ])
def index():
    return 'First request'

@app.route('/flipacoin', methods=[ 'GET' ])
def flipacoin():
    return choice(['Cara', 'Coroa'])

@app.route('/registername', methods=[ 'POST' ])
def registername():
    data=request.get_json()
    query="INSERT INTO usuario(name) VALUES(%s)"
    values=(data["name"],)
    cursor.execute(query,values)
    return 'Inserido com sucesso'    

if __name__ == '__main__':

    current_module = os.path.dirname(os.path.curdir)
    sys.path.append(current_module)

    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'development'   
    

    app.run(host='0.0.0.0',port='8080')

    
