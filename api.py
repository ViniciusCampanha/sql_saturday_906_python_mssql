
import os
import sys

import flask 

import blueprints.test

from random import choice

app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(blueprints.test.blueprint)


@app.route('/', methods=[ 'GET' ])
def index():
    return 'First request'

@app.route('/flipacoin', methods=[ 'GET' ])
def flipacoin():
    return choice(['Cara', 'Coroa'])

@app.route('/registername', methods=[ 'POST' ])
def registername():
    

if __name__ == '__main__':

    current_module = os.path.dirname(os.path.curdir)
    sys.path.append(current_module)

    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'development'

    app.run(host='0.0.0.0',port='8080')

    
