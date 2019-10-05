import os
import pymssql

dbconn = pymssql.connect(
    server=r'localhost',
    user=r'python',
    password='Pyth0n$2019',
    database='master'
)