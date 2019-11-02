import mysql.connector
import os

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

USER=os.environ['USER']
PASSWORD=os.environ['PASSWORD']
HOST=os.environ['HOST']
DATABASE=os.environ['DATABASE']

def lambda_handler(event, context):

    print('----- environment variables -----')
    print(os.environ)

    print('----- db query -----')
    cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
    cursor = cnx.cursor()
    query = ("show databases")
    cursor.execute(query)
    print(cursor)

    for (db) in cursor:
        print(db)

    return "ok"