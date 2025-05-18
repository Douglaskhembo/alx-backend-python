import mysql.connector
from mysql.connector import Error
from decimal import Decimal
from contextlib import contextmanager

@contextmanager
def get_connection_cursor():
    connection = mysql.connector.connect(
        host='localhost',
        user='Admin',
        password='@MeconE_21',
        database='ALX_prodev'
    )
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
    finally:
        cursor.close()
        if connection.is_connected():
            connection.close()

def stream_users():
    with get_connection_cursor() as cursor:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            if isinstance(row.get('age'), Decimal):
                row['age'] = int(row['age'])
            yield row
