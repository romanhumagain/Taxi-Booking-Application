from Controller.connection import  mysql_connection

def validate_credentials(email, password):
    try:
        connection = mysql_connection()
        if connection is not None:
            # create a cursor object
            cursor = connection.cursor()

            # sql query to insert data into the table
            search_query = """SELECT * FROM user WHERE email =%s and password = %s  """
            values = (email, password)

            # to execute the query
            cursor.execute(search_query, values)
            user = cursor.fetchone()

            # return true if user exists else false
            return user is not None

    except Exception as error:
        print(f"ERROR {error}")
        return False

    finally:
        cursor.close()
        connection.close()
