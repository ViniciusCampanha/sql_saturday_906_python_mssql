
import os
import sys

import flask

import blueprints.backup
import blueprints.database

app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(blueprints.backup.blueprint)
app.register_blueprint(blueprints.database.blueprint)

@app.route('/', methods=[ 'GET' ])
def index():
    return flask.redirect('/index.html')
    
if __name__ == '__main__':

    current_module = os.path.dirname(os.path.curdir)
    sys.path.append(current_module)

    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'development'

    app.run(host='0.0.0.0',port='8080')