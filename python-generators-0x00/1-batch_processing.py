import mysql.connector
from decimal import Decimal

def stream_users_in_batches(batch_size):
    """Generator to fetch users from database in batches of batch_size."""
    connection = None
    cursor = None
    offset = 0
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='Admin',
            password='@MeconE_21',
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)

        while True:
            query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
            cursor.execute(query, (batch_size, offset))
            batch = cursor.fetchall()
            if not batch:
                break
            # convert Decimal age to int for each row
            for row in batch:
                if isinstance(row.get('age'), Decimal):
                    row['age'] = int(row['age'])
            yield batch
            offset += batch_size
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

def batch_processing(batch_size):
    """Process batches to filter users over the age of 25 and yield them one by one."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user.get('age', 0) > 25:
                yield user
