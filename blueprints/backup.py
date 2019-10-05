import flask
import pymssql
from flask import jsonify, request

from config import dbconn

blueprint = flask.Blueprint('backup', __name__)

dbconn.autocommit(True)
cursor = dbconn.cursor()

@blueprint.route('/backup/create', methods=[ 'POST' ])
def backup_database():

    data = request.get_json()

    database = data['database']
    mode = data['mode']
    device = data['device']

    if mode == 'FULL':
        command = "BACKUP DATABASE [" + database + "] TO [" + device + "] WITH COMPRESSION, CHECKSUM;"
    elif mode == 'DIFF':
        command = "BACKUP DATABASE [" + database + "] TO [" + device + "] WITH DIFFERENTIAL, COMPRESSION, CHECKSUM;"
    elif mode == 'INCR':
        command = "BACKUP LOG [" + database + "] TO [" + device + "] WITH COMPRESSION;"
    else:
        return jsonify({'result': 'Comando de backup não existe. Utilize: FULL, DIFF, INCR'})
  
    cursor.execute(command)
    return jsonify({'result': 'Backup ' + mode +' gerado com sucesso!', 'comando': command})

    dbconn.autocommit(False)
    dbconn.close()