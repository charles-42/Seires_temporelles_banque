from dotenv import load_dotenv
from sqlalchemy import create_engine

import os

def get_engine():

    load_dotenv()

    params = f"Driver={os.environ.get('driver')};Server=tcp:{os.environ.get('server')},1433;Database={os.environ.get('database')};Uid={os.environ.get('username')};Pwd={os.environ.get('password')};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'"
    conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    engine = create_engine(conn_str,echo=True)

    print('connection is ok')
    return engine

def get_engine_master():

    load_dotenv()

    params = f"Driver={os.environ.get('driver')};Server=tcp:{os.environ.get('server')},1433;Database=master;Uid={os.environ.get('username')};Pwd={os.environ.get('password')};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'"
    conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    engine = create_engine(conn_str,echo=True)

    print('connection is ok')
    return engine