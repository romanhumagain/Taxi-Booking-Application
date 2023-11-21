from Controller.connection import mysql_connection

# ================== TO INSERT RECORD TO THE Account Activity TABLE ====================
def insert_account_activity_details(accountActivity):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()

            # query for insert
            query = """INSERT INTO account_activity(activity_related, description, date, time, user_id) VALUES (%s, %s, %s, %s, %s)"""
            values = (
                accountActivity.get_activity_related(),
                accountActivity.get_description(),
                accountActivity.get_date(),
                accountActivity.get_time(),
                accountActivity.get_user_id()
            )

            cursor.execute(query, values)
            print("second")


            connection.commit()

            return True
    except Exception as e:
        print(f"ERROR {e}")
        return False
    finally:
        cursor.close()
        connection.close()


# =============== TO FETCH THE ACCOUNT DETAILS FROM THE DATABASE =========================
def fetch_account_activity_details(accountActivity):
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query  = "SELECT * FROM account_activity WHERE user_id = %s ORDER BY activity_id DESC"
            values =(accountActivity.get_user_id(),)

            cursor.execute(query, values)
            result = cursor.fetchall()

    except Exception as error:
        print(f"ERROR:- {error}")

    finally:
        cursor.close()
        connection.close()
        return result
