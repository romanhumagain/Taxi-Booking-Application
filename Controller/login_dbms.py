from Controller.connection import  mysql_connection
from Model.Global import *
def validate_credentials(email, password):
    user = None
    customer = None
    try:
        connection = mysql_connection()
        if connection is not None:
            # create a cursor object
            cursor = connection.cursor()

            # sql query to insert data into the table
            search_query = """SELECT * FROM user WHERE email = %s and password = %s"""
            values = (email, password)

            # to execute the query
            cursor.execute(search_query, values)
            user = cursor.fetchone()
            if user is not None:
                cursor.execute("SELECT * FROM customer WHERE user_id = %s", (user[0],))
                customer = cursor.fetchone()

    except Exception as error:
        print(f"ERROR {error}")

    finally:
        cursor.close()
        connection.close()
        return user, customer



