import pymssql
import json

conn = pymssql.connect(
    server=r'localhost',
    user=r'sa',
    password='Xt000018$',
    database='master'
)

conn.autocommit(True)
cursor = conn.cursor()

def create_database(database):

    command = 'CREATE DATABASE ' + database + ';'
    cursor.execute(command)
    cursor.execute('select name, state_desc from sys.databases where name = %s',database)
    row = cursor.fetchone()

    print(row)

    conn.autocommit(False)
    conn.close()

def drop_database(database):

    command = 'DROP DATABASE ' + database + ';'
    cursor.execute(command)

    conn.autocommit(False)
    conn.close()


def backup_database(database,mode,path):

    print(path)

    device = path + database

    if mode == 'FULL':
        command = "BACKUP DATABASE [" + database + "] TO DISK = '" + device + ".bak' WITH COMPRESSION, CHECKSUM;"
    elif mode == 'DIFF':
        command = "BACKUP DATABASE [" + database + "] TO DISK = '" + device + ".dif' WITH DIFFERENTIAL, COMPRESSION;"
    elif mode == 'INCR':
        command = "BACKUP LOG [" + database + "] TO DISK = '" + device + ".log' WITH COMPRESSION;"

    print(command)

    cursor.execute(command)

    conn.autocommit(False)
    conn.close()

def restore_database(database,mode,path):

    print(path)

    device = path + database

    if mode == 'FULL':
        command = "RESTORE DATABASE [" + database + "] TO DISK = '" + device + ".bak' WITH COMPRESSION, CHECKSUM;"
    elif mode == 'DIFF':
        command = "RESTORE DATABASE [" + database + "] TO DISK = '" + device + ".dif' WITH DIFFERENTIAL, COMPRESSION;"
    elif mode == 'INCR':
        command = "RESTORE LOG [" + database + "] TO DISK = '" + device + ".log' WITH COMPRESSION;"

    print(command)

    cursor.execute(command)

    conn.autocommit(False)
    conn.close()

#create_database('SQLSAT')
#backup_database('DBS600','FULL','C:\\temp\\')
drop_database('SQLSAT')