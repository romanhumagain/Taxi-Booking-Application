from Controller.connection import mysql_connection
from Model.user import User

# ======================== TO CHANGE THE USER PASSWORD ============================

def change_user_password(user):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """UPDATE user SET password = %s WHERE user_id = %s """
            values = (user.get_password(), user.get_user_id())

            # to execute the query
            cursor.execute(query, values)
            connection.commit()

            return True

    except Exception as error:
        print(f"ERROR: {error}")
        return False

    finally:
        cursor.close()
        connection.close()

