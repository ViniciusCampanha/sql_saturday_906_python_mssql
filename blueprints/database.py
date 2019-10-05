import flask
from flask import jsonify

from config import dbconn

blueprint = flask.Blueprint('database', __name__)

dbconn.autocommit(True)
cursor = dbconn.cursor()

@blueprint.route('/database/create/<database>', methods=[ 'POST' ])
def create_database(database):

    command = 'CREATE DATABASE ' + database + ';'
    cursor.execute(command)
    cursor.execute('select name, state_desc from sys.databases where name = %s',database)
    row = cursor.fetchone()

    return jsonify(
        name = row[0],
        status = row[1],
        status_comando = 'Banco de Dados criado com sucesso.'
    )

    dbconn.autocommit(False)
    dbconn.close()

@blueprint.route('/database/drop/<database>', methods=[ 'POST' ])
def drop_database(database):

    command = 'DROP DATABASE ' + database + ';'
    cursor.execute(command)

    return jsonify(
        status_comando = 'Banco de Dados dropado com sucesso.'
    )

    dbconn.autocommit(False)
    dbconn.close()
