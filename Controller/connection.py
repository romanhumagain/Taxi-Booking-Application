import mysql.connector
import os

def mysql_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            database='taxi_booking_system',
            host='localhost',
            user='root',
            password=""
        )
        return connection

    except Exception as error:
        print(f"ERROR: {error}")
        return connection
