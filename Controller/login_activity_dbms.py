from Controller.connection import mysql_connection

# =============== TO INSERT THE LOGIN DETAILS IN THE DATABASE =======================
def store_login_details(loginActivity):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()

            # query for insert
            query = """INSERT INTO loginactivity(device_type, os, processor, node_device_name,login_date, login_time, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            values = (
                loginActivity.get_device_type(),
                loginActivity.get_os(),
                loginActivity.get_processor(),
                loginActivity.get_node_device_name(),
                loginActivity.get_login_date(),
                loginActivity.get_login_time(),
                loginActivity.get_user_id()
            )
            cursor.execute(query, values)
            connection.commit()

            return True
    except Exception as e:
        print(f"ERROR {e}")
        return False
    finally:
        cursor.close()
        connection.close()



# =============== TO FETCH THE LOGIN DETAILS FROM THE DATABASE =========================
def fetch_login_details(loginActivity):
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query  = "SELECT * FROM loginactivity WHERE user_id = %s ORDER BY activity_id DESC"
            values =(loginActivity.get_user_id(),)

            cursor.execute(query, values)
            result = cursor.fetchall()

    except Exception as error:
        print(f"ERROR:- {error}")

    finally:
        cursor.close()
        connection.close()
        return result

