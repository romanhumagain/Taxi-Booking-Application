from Controller.connection import  mysql_connection
from Model.Global import *
def validate_credentials(email, password):
    connection = None
    cursor = None
    user = None
    customer = None
    driver = None
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
            print(user)
            if user is not None:
                if user[3] == "customer":
                    cursor.execute("SELECT * FROM customer WHERE user_id = %s", (user[0],))
                    customer = cursor.fetchone()

                elif user[3] == "driver":
                    cursor.execute("SELECT * FROM driver WHERE user_id = %s", (user[0],))
                    driver = cursor.fetchone()

                elif user[3] == "admin":
                    pass

    except Exception as error:
        print(f"ERROR {error}")

    finally:
        cursor.close()
        connection.close()
        return user, customer, driver



